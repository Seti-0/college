import sqlalchemy as sqla
from sqlalchemy import create_engine
import requests
import time
import config
import pandas as pd
import datetime
import traceback


URL = "http://api.openweathermap.org/data/2.5/forecast?q=dublin,ie&appid={}".format(config.OWKEY)

metadata = sqla.MetaData()
engine = config.CONNECTION_STRING



def download_data(url):
    """Gets weather forecast for Dublin for 3 hour intervals over next five days.
    Takes only weather information from return object and return information as Python array."""
    response = requests.get(url)
    data = response.json()

    if not response.ok:
        print("Error Code:", response.status_code)
        print("Reason:", response.reason)

    return data


def convert_data(data):
    """Takes only necessary data points from weather information, flattens internal dictionary objects, labels columns.
    Returns cleaned data as dataframe."""
    records = []
    for datum in data['list']:
        records.append({'date_time': datetime.datetime.fromtimestamp(datum['dt']),
         'clouds_all': datum['clouds']['all'],
         'feels_like': datum['main']['feels_like'],
         'humidity': datum['main']['humidity'],
         'pressure': datum['main']['pressure'],
         'temp': datum['main']['temp'],
         'temp_max': datum['main']['temp_max'],
         'temp_min': datum['main']['temp_min'],
         'description': datum['weather'][0]['description'],
         'main_description': datum['weather'][0]['main'],
         'wind_speed': datum['wind']['speed'],
         'wind_deg': datum['wind']['deg'],
            'sunrise': datetime.datetime.fromtimestamp(data['city']['sunrise']),
            'sunset': datetime.datetime.fromtimestamp(data['city']['sunset'])})

    return pd.DataFrame.from_records(records)


def main():
    """Downloads and converts data before sending to remote database.
    Repeats every three hours and overwrites table each time, so forecast data is always up to date."""
    while True:
        try:
            data = download_data(URL)
            df = convert_data(data)
            df.to_sql('five_day_forecast', engine, if_exists='replace', index=False)
            time.sleep(60*60*3)
        except:
            print(traceback.format_exc())


if __name__ == "__main__":
   main()

