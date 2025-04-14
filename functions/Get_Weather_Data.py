import pandas as pd
from Open_meteo_connection import get_response
from Geo_location import geo_locate

connection=get_response("San Diego", "2023-06-01", "2023-06-08")

def get_weather_data(response):
	hourly_data = response.Hourly()
	Temp_data=hourly_data.Variables(0).ValuesAsNumpy()
	timestamp=hourly_data.Time()
	converted_timestamp = pd.to_datetime(timestamp, unit='s')
	length=len(Temp_data)
	timestamps = pd.date_range(start=converted_timestamp, periods=len(Temp_data), freq="h")

	Temp_df = pd.DataFrame({'Timestamp': timestamps, 'Temperature': Temp_data})
	#convert temperature to fahrenheit
	Temp_df['Temperature'] = Temp_df['Temperature'] * 9/5 + 32

	print(Temp_df.head())


if connection:
    get_weather_data(connection)
else:
    print("Weather data fetch skipped.")