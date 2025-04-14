
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from Geo_location import geo_locate

def get_response(name,start_date,end_date):
    # Set up a cache for the requests to caputre response each hour
	cache=requests_cache.CachedSession('.cache', expire_after=3600)

	#Set up mechanism to retry on error
	Rt=retry(cache, retries=5, backoff_factor=0.2)

	# Set up the Open Meteo API connection
	openmeteo_wrapper=openmeteo_requests.Client(session=Rt)
	location_info=geo_locate(name)
	if location_info:
		latitude=location_info['latitude']
		longitude=location_info['longitude']
	dates={"start_date": start_date, "end_date": end_date}

	#Set up url connection and parameters
	historical_url="https://archive-api.open-meteo.com/v1/archive"
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"start_date": f"{dates['start_date']}",
		"end_date": f"{dates['end_date']}",
    	"hourly": "temperature_2m"
	}

	historical_responses = openmeteo_wrapper.weather_api(historical_url, params=params)

	return historical_responses[0]


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

try:
	get_weather_data(connection)
except Exception as e:
	print(f"An error occurred: Please enter a valid response")


