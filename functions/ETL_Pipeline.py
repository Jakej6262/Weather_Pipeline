from Open_meteo_connection import get_response
from Get_Weather_Data import get_weather_data
import pandas as pd

def ETL(name, start_date, end_date):
    
    # Extract
    response = get_response(name, start_date, end_date)
    
    # Transform
    if response:
        weather_data = get_weather_data(response)
        if weather_data is not None:
            # Load
            print("Weather data fetched successfully.")
            print(weather_data.head())
            # Save to CSV
            #weather_data.to_csv(f"{name}_weather_data.csv", index=False)

    
    else:
        print("Weather data fetch skipped.")
        return None
    

    

ETL("Seattle", "2023-04-01", "2023-04-08")