import pandas as pd

# Read the CSV file into a DataFrame
coin_timeframe = 'btc_4h'
df = pd.read_csv(f'experiment/0_historical_data/{coin_timeframe}_original.csv')

# Convert the time-related columns to datetime format
df['time_period_start'] = pd.to_datetime(df['time_period_start'])
df['time_period_end'] = pd.to_datetime(df['time_period_end'])
# df['time_open'] = pd.to_datetime(df['time_open'])
# df['time_close'] = pd.to_datetime(df['time_close'])

# Specify the start and end times for filtering
start_time = pd.to_datetime('2022-12-01 00:00:00').tz_localize('UTC')
end_time = pd.to_datetime('2023-12-20 00:00:00').tz_localize('UTC')

# Filter the DataFrame based on the specified time period
# filtered_df = df[(df['time_period_start'] >= start_time) & (df['time_period_end'] <= end_time)]
filtered_df = df[(df['time_period_start'] >= start_time) ]

# Write the filtered DataFrame to a new CSV file
output_path = f'experiment/0_historical_data_period3/{coin_timeframe}.csv'
filtered_df.to_csv(output_path, index=False)

print("Filtered data has been written to " + output_path)
