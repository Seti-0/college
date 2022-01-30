from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import config
from prediction2 import get_bike_predictions


app = Flask(__name__)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
db = SQLAlchemy()


def init_db(connection_str):
    """
    Initialize the database.

    This is exposed as a function so
    that a different database might
    be used when testing.
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_str
    db.init_app(app)


@app.route("/favicon.ico")
def get_title_icon():
    """
    This is the icon that is displayed by
    the browser beside the tab title.
    """
    return send_from_directory("static/icons", "bicycle-icons8.ico")


@app.route("/")
def index():
    """Get the home page."""
    return send_from_directory("static/html", "index.html")


@app.route("/about")
def about():
    """Get the about page"""
    return send_from_directory("static/html", "about.html")



@app.route("/stations/static")
def stations():
    """Get static data for all stations, in json."""
    query = "SELECT * FROM stations"
    return query_database(query)


@app.route("/stations/latest")
def station_updates_latest():
    """
    Get the latest retrieved data for
    all stations, in json.
    Static data is included as well!
    """
    query = "CALL stations_latest"
    return query_database(query, output_index="number")


@app.route("/stations/template")
def station_template():
    """
    Get a template HTML snippet for use as
    content in the station info popups.
    """
    return send_from_directory("static", "html/station_template.html")


@app.route("/weather/data")
def get_weather_data():
    """
    Get the current weather for Dublin and for the next four/five days from database, dependent on availability of
    forecast in database.
    Returns a dictionary with integer indexes as keys to
    nested dictionary values with the date in datetime format, the rounded 'feels like' temperature and main description.
    """
    query = "CALL get_weather_data"
    df = pd.read_sql(query, db.engine)
    data = {}
    for i, row in df.iterrows():
        data[i] = {'date': row['date'], 'temp': row['temp'], 'description': row['description']}

    return data


@app.route("/weather/icons/<description>")
def get_weather_icon(description):
    """
    :param description: String, corresponding to main description for current weather or forecast
    :return: corresponding icon from icons/weather

    If it can't find a matching icon for the description, it defaults to returning a cloudy icon. Cos y'know, Dublin.
    """

    mapping = {
        "Rain": "icons8-rain-25.png",
        "Snow": "icons8-snow-25.png",
        "Clear": "icons8-sun-25.png",
        "Drizzle": "icons8-rain_cloud.png",
        "Clouds": "icons8-partly-cloudy-day-25.png"
    }

    if description in mapping.keys():
        return send_from_directory("static/icons/weather", mapping[description])
    else:
        return send_from_directory("static/icons/weather", "icons8-clouds-25.png")


@app.route("/stations/prediction")
def get_predictions():
    """
    Request to above URL endpoint should be formatted /stations/prediction?numbers=1,2,3&date=2021-03-04&hour=18
    where date is in YYYY-MM-DD string format and hour is integer 0-23.

    Returns dictionary of station numbers with the predicted availability for the date and time.
    """

    date = request.args.get('date')
    time = request.args.get('hour')

    return get_bike_predictions(date, time, db.engine)


def query_database(query: str, output_index=None):
    """
    Accepts sql query as string and optional output index as string name of column to use as output index.
    Query the database using the flask alchemy database, created above.
    If no output index is provided, returns a dictionary of lists where keys are field names,
    otherwise returns dictionary of dictionaries with values from column name provided as keys.
    """

    df = pd.read_sql(query, db.engine)

    if output_index is not None:
        result = df.set_index(output_index).to_json(orient="index")

    else:
        # "to_json" would be slightly shorter here,
        # but this seems a friendlier then any of the formats
        # that function gives.
        result = dict()
        result["rowcount"] = len(df)
        for field in df:
            result[field] = df[field].values.tolist()

    return result


@app.route("/charts/average/<int:station_num>")
def chart_avail(station_num):
    """
    Generate JSON data endpoint based on station number passed into sql query. This data is used to chart
    usage statistics for different stations.
    """

    sql = f"""
    -- Average bikes (full/empty) by hour
       SELECT 
        bike.number,
        bike.bike_stands,
        ROUND(AVG(bike.available_bikes), 0) AS avg_avail_bikes,
        bike.bike_stands - ROUND(AVG(bike.available_bikes), 0) AS avg_avail_spaces,
        HOUR(retrieved) as `hour`,
        CASE
            WHEN DAYOFWEEK(retrieved) = 1 THEN 'Sunday'
            WHEN DAYOFWEEK(retrieved) = 2 THEN 'Monday'
            WHEN DAYOFWEEK(retrieved) = 3 THEN 'Tuesday'
            WHEN DAYOFWEEK(retrieved) = 4 THEN 'Wednesday'
            WHEN DAYOFWEEK(retrieved) = 5 THEN 'Thursday'
            WHEN DAYOFWEEK(retrieved) = 6 THEN 'Friday'
            WHEN DAYOFWEEK(retrieved) = 7 THEN 'Saturday'
            WHEN DAYOFWEEK(retrieved) = 8 THEN 'Sunday'
        END AS weekday
    FROM
        sebikes.station_update bike
    WHERE
        bike.number = { station_num } 
            AND DAYOFWEEK(retrieved) = DAYOFWEEK(CURDATE())
            AND HOUR(retrieved) > 5 
            AND HOUR(retrieved) < 23
    GROUP BY `hour`
    ORDER BY `hour`; 
        """

    df = pd.read_sql(sql, con=db.engine)
    json_results = df.to_json(orient='records', index=True)
    return json_results


@app.route("/charts/today/<int:station_num>")
def chart_avail_today(station_num):
    """
    Generate JSON data endpoint based on station number passed into sql query. This data is used to chart
    usage statistics for different stations.
    """

    sql = f"""
    -- Average bikes (full/empty) today
    SELECT 
        bike.number,
        round(AVG(bike.available_bikes),0) AS avg_avail_bikes,
        bike.bike_stands - round(AVG(bike.available_bikes),0) AS avg_avail_spaces,
        HOUR(retrieved) as `hour`
    FROM
        sebikes.station_update bike
    WHERE
        bike.number = {station_num} and
        DATE(retrieved) = curdate()
    GROUP BY `hour`;
        """

    df = pd.read_sql(sql, con=db.engine)
    json_results = df.to_json(orient='records', index=True)
    return json_results


if __name__ == "__main__":

    init_db(config.CONNECTION_STRING)

    # Run the app in debug mode.
    app.run(debug=False, host="0.0.0.0")

    # Note: even without debug mode, app.run
    # is apparently not the way the app should
    # be deployed in a production setting?
