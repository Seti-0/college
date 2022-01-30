import sqlalchemy as sqla
from sqlalchemy import create_engine
from pprint import pprint
import requests
import time
import config
import pandas as pd
import datetime
import traceback

URL = "http://api.openweathermap.org/data/2.5/weather?q=dublin,ie&appid={}"

metadata = sqla.MetaData()
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(config.USER, config.PASSWORD, config.URI, config.PORT, config.DB), echo=True)

def get_weather_data():
    r = requests.get(URL.format(config.OWKEY)).json()
    data = [{'date_time': datetime.datetime.fromtimestamp(r['dt']),
                 'clouds_all': r['clouds']['all'],
                 'cod': r['cod'],
                 'feels_like': r['main']['feels_like'],
                 'humidity': r['main']['humidity'],
                 'pressure': r['main']['pressure'],
                 'temp': r['main']['temp'],
                 'temp_max': r['main']['temp_max'],
                 'temp_min': r['main']['temp_min'],
                 'sunrise': datetime.datetime.fromtimestamp(r['sys']['sunrise']),
                 'sunset': datetime.datetime.fromtimestamp(r['sys']['sunset']),
                 'description': r['weather'][0]['description'],
                 'main_description': r['weather'][0]['main'],
                 'wind_speed': r['wind']['speed'],
                 'wind_deg': r['wind']['deg']}]

    return data


def store(data):
    df = pd.DataFrame.from_records(data)
    df.to_sql('dublin_weather', engine, if_exists='append', index=False)


def main():
    while True:
        try:
            data = get_weather_data()
            store(data)
            time.sleep(60*60)
        except:
            print(traceback.format_exc())


if __name__ == "__main__":
    main()

