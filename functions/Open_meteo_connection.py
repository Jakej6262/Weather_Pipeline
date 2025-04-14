
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

	if not location_info:
		print("Location selection cancelled or failed.")
		return None  # Exit cleanly
	
	
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




