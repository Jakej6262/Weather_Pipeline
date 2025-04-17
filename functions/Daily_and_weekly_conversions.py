def convert_to_daily(dataframe):
    # Step 1: Convert 'Timestamp' to datetime
    dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])

    # Step 2: Set 'Timestamp' as the index
    dataframe.set_index('Timestamp', inplace=True)

    # Step 3: Resample to daily totals
    daily_df = dataframe.resample('D').agg({
    'Temperature': 'mean',      
    'Feels like': 'mean',        
    'Humidity': 'mean',          
    'Precipitation': 'sum'       
    })

    # Step 4: Reset index to make 'Timestamp' a column again
    daily_df.reset_index(inplace=True)
    print(daily_df.head())
    return daily_df

def convert_to_weekly(dataframe):
     # Step 1: Convert 'Timestamp' to datetime
    dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])

    # Step 2: Set 'Timestamp' as the index
    dataframe.set_index('Timestamp', inplace=True)

    # Step 3: Resample to daily totals
    weekly_df = dataframe.resample('W').agg({
    'Temperature': 'mean',      
    'Feels like': 'mean',        
    'Humidity': 'mean',          
    'Precipitation': 'sum'       
    })

    # Step 4: Reset index to make 'Timestamp' a column again
    weekly_df.reset_index(inplace=True)
    print(weekly_df.head())
    return weekly_df


