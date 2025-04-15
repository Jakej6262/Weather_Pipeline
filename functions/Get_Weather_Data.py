import pandas as pd
from Open_meteo_connection import get_response
from Geo_location import geo_locate


def get_weather_data(response):
	hourly_data = response.Hourly()
	Temp_data=hourly_data.Variables(0).ValuesAsNumpy()
	timestamp=hourly_data.Time()
	hourly_relative_humidity = hourly_data.Variables(1).ValuesAsNumpy()
	hourly_precipitation = hourly_data.Variables(2).ValuesAsNumpy()
	hourly_apparent_temperature = hourly_data.Variables(3).ValuesAsNumpy()
	hourly_rain = hourly_data.Variables(4).ValuesAsNumpy()
	hourly_snowfall = hourly_data.Variables(5).ValuesAsNumpy()
	hourly_snow_depth = hourly_data.Variables(6).ValuesAsNumpy()

	converted_timestamp = pd.to_datetime(timestamp, unit='s')
	length=len(Temp_data)
	timestamps = pd.date_range(start=converted_timestamp, periods=len(Temp_data), freq="h")

	Temp_df = pd.DataFrame({'Timestamp': timestamps, 'Temperature': Temp_data, 'Feels like': hourly_apparent_temperature, 'Humidity': hourly_relative_humidity, 'Precipitation': hourly_precipitation})
	#convert temperature to fahrenheit
	Temp_df['Temperature'] = Temp_df['Temperature'] * 9/5 + 32

	return Temp_df


