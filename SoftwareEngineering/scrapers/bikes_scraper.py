import pandas as pd
import requests
import datetime
import config
import logging


WAIT_TIME = 5*60 # seconds

TARGET_TABLE = "station_update"
URL = "https://api.jcdecaux.com/vls/v1/stations?contract=dublin"

# The API key must be sent with the request.
URL += "&apiKey=" + config.JCDECAUX_API_KEY

EXPECTED_FIELDS = ["number", "banking", "bonus", "bike_stands", "available_bikes", "status", "last_update"]
KEY = "number" # If this field is missing, the record is dropped.
TO_CONVERT = ["last_update"]
RETRIEVAL_DATE_FIELD = "retrieved"


def convert_dates(data, date_field_names):
   
    """
    Given a pandas DataFrame, converts any date fields
    from the JCDecaux format to a python-friendly format.
    """
    
    # This is a curious one.
    # JCDecaux encodes its dates in the integer format
    # used by the "Date" object in javascript.
    
    # This is defined as the number of milliseconds since
    # the 1st of the 1st, 1970. This can be expressed directly
    # with python's datetime and timedelta objects.

    def convert(jcdecaux_date):

        python_date = datetime.datetime(1970, 1, 1) 
        python_date += datetime.timedelta(milliseconds=jcdecaux_date)
        return python_date

    # The conversion will fail if there are missing 
    # values, for example.
    failed_count = 0

    for field in date_field_names:
        for i in range(len(data)):
            try:
                data.at[i, field] = convert(data.at[i, field])
            except:
                failed_count += 1

    if failed_count > 0:
        logging.warning(f"Failed to convert {failed_count} date values")
    

def clean(json, expected_fields, key_name):
    
    """
    Takes in a json string. Parses and cleans it, returns
    a pandas DataFrame.
    
    Unexpected columns are dropped. Missing values
    are assumed null, unless the field in question is 
    the key. In this case, the entire record with the missing
    value is dropped.
    """
    
    data = pd.read_json(json)

    # Add missing columns.
    
    for field in expected_fields:
        if field not in data:
            data[field] = None 
    
    # Discard extra columns

    data = data[expected_fields]

    # Check for rows missing the key.
    
    rows_before = data.shape[0]
    data = data.dropna(subset=[key_name])
    rows_after = data.shape[0]
    
    rows_dropped = rows_before - rows_after
    if rows_dropped > 0:
        logging.warning(f"Skipping {rows_dropped} rows due to missing key!")
    
    # Tally missing values

    missing_count = data.isna().values.sum()
    if missing_count > 0:
        logging.warning(f"Detected {missing_count} missing values.")

    # All done, return.

    return data

    
def main():
    
    """
    Download updates to bike station data and add
    them to the database station_update table.

    If the table does not exist, it is created.
    However, it is created without a primary key! 
    If a primary key is needed it should be added 
    in later.

    If the table does exist, it is appended to.
    """
    
    response = requests.get(URL)
    
    if not response.ok:
        logging.warning(f"Error Code: {response.status_code}")
        logging.warning(f"Reason: {response.reason}")
        return False
    
    data = clean(response.content, EXPECTED_FIELDS, KEY)

    convert_dates(data, TO_CONVERT)
    data[RETRIEVAL_DATE_FIELD] = datetime.datetime.now()
    
    data.to_sql(TARGET_TABLE, config.CONNECTION_STRING, 
        if_exists="append", index=False)
    

if __name__ == "__main__":

    import scheduler
    scheduler.schedule(main, WAIT_TIME)