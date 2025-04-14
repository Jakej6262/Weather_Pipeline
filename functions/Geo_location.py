#import required libraries
import requests
import requests_cache
from retry_requests import retry
import pandas as pd

def geo_locate(name):
    # Set up a cache for the requests to caputre response each hour
    cache=requests_cache.CachedSession('.geocache', expire_after=3600)
    rt=retry(cache, retries=5, backoff_factor=0.2)
    # Set up the Open Meteo API connection
    endpoint='https://geocoding-api.open-meteo.com/v1/search'
    params = {"name": name}
    # Call the API and get the response
    try:
        response=rt.get(endpoint, params=params)
        data=response.json()

        if 'results' not in data or len(data['results']) == 0:
            print(f"No locations found for {name} ")
            return None

        results=data['results']
        
        
        for i, result in enumerate(results,1):
        
            print(f"Option {i}: {result['name']} {result['admin1']} {result['country']}")
        
        while True:
            try:
                input_option=int(input("Select an Option # or 0 to cancel: "))

                if input_option==0:
                    break
               
                
                if 1 <= input_option <= len(results):
                    selection=results[input_option-1]
                    info_dict={"name": f"{selection['name']} {selection['admin1']} {selection['country']}", "latitude": selection['latitude'], "longitude": selection['longitude']}
                    return info_dict
                else:
                    print("Choose a value within the list of options")
                    continue

            
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
               
       
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None
        


    

    


