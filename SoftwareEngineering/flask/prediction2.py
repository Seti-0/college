import pandas as pd
import pickle

# dictionary of models, one for each station, stored by <number: model>.Models last trained/updated, April 12th 2021
models = pickle.load(open('models_v2.sav', 'rb'))
# Scaler fitted to original weather data used to train models, input weather needs to be normed to use nn model.
weather_scaler = pickle.load(open('scaler_v2.sav', 'rb'))


def get_bike_predictions(date, time, connection):
    """
    :param date: string YYYY-MM-DD format
    :param time: integer 0-23
    :param connection: db string or engine to use for connection
    :return: dictionary with station numbers as keys, and predicted availability as values
    """

    # These lines retrieve the relevant weather data from the database to base the predictions on
    forecast_sql = f"""
    SELECT 
        DAYOFWEEK(date_time) as day, 
        CAST(date_time AS time) as time, 
        HOUR(date_time) as hour, 
        CAST(sunrise AS time) as sunrise, 
        CAST(sunset as time) as sunset, 
        main_description, 
        wind_speed, 
        ROUND(feels_like - 270) as temp
    FROM five_day_forecast
    WHERE DATE(date_time) = DATE("{date}") AND (HOUR(date_time) = {time} OR HOUR(date_time) = {time} - 1 OR HOUR(date_time) = {time} - 2);"""
    forecast = pd.read_sql(forecast_sql, connection)

    # These lines transform the fetched weather data so it can used in machine learning
    forecast['is_workday'] = (1 < forecast.day) & (forecast.day < 7) * 1.0
    rain_yn = []
    for description in forecast['main_description']:
        rain_yn.append('rain' in description.lower())
    forecast['rain_yn'] = rain_yn
    forecast['daytime'] = (forecast.time > forecast.sunrise) & (forecast.time < forecast.sunset)
    forecast['morning-rush'] = (int(time) >= 8) & (int(time) < 10) & (forecast.is_workday == 1)
    forecast['evening-rush'] = (int(time) >= 4) & (int(time) < 7) & (forecast.is_workday == 1)

    forecast.drop(['day', 'main_description', 'time', 'hour', 'sunrise', 'sunset'], axis='columns', inplace=True)

    # Normalise weather forecast in line with data in nearest neighbours model
    normed_forecast = weather_scaler.transform(forecast)

    predictions = {}

    for key, item in models.items():
        predictions[key] = round(item.predict(normed_forecast)[0])

    return predictions


