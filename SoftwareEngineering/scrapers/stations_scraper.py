import requests
import pandas as pd


# This is a once off setup & occasional 
# update - there is no need for logging, 
# and it does not have to be run from EC2.


from config import CONNECTION_STRING
URL = "https://developer.jcdecaux.com/rest/vls/stations/dublin.json"
TABLE_NAME = "stations"


def main():

    """
    Update the database defined in config.py with static bike
    station information from JCDecaux. 
    
    If the target table does not yet exist, it will be created.
    However, it will be created without a primary key! The key
    should be added afterwards if it is needed.

    If the target table exists, it will be replaced.
    """
    
    print("Updating static station data.")
    print("Downloading data from", URL)

    data = download_data(URL)
    if data is None:
        return

    data.to_sql(TABLE_NAME, CONNECTION_STRING, 
        if_exists="replace", index = False)
        
    print("Update complete.")
 

def download_data(url):
    
    response = requests.get(url)
    
    if not response.ok:
        print("Error Code:", response.status_code)
        print("Reason:", response.reason)
    
    data = pd.read_json(response.content)
    return data


if __name__ == "__main__": 
    main()
