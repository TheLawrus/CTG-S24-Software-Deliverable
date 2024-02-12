from datetime import datetime, timedelta
import os
import pandas as pd


def combine_volume_adjusted_momentums(path):
    volume_adjusted_momentum_df = pd.DataFrame()

    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(path, filename))
            df = df[['Date', 'Close', 'Volume']]

            temp_ticker_df = pd.DataFrame()
            temp_ticker_df['Date'] = df['Date']
            ticker_name = filename.split('.')[0]
            temp_ticker_df[ticker_name] = None

            for index, row in df.iterrows():
                date = row['Date']
                volume_adjusted_momentum = calculate_volume_adjusted_momentum(date, df)
                temp_ticker_df.at[index, ticker_name] = volume_adjusted_momentum

            if volume_adjusted_momentum_df.empty:
                volume_adjusted_momentum_df = temp_ticker_df
            else:
                volume_adjusted_momentum_df = pd.merge(volume_adjusted_momentum_df, temp_ticker_df, on='Date', how='inner')

    volume_adjusted_momentum_df.set_index('Date', inplace=True)
    volume_adjusted_momentum_df.to_csv('volume_adjusted_momentum.csv')


def calculate_volume_adjusted_momentum(date, df):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')

    prev_day = datetime_obj - timedelta(days=1)
    period_start = prev_day - timedelta(days=15)

    prev_day_close = df.loc[df['Date'] == prev_day.strftime('%Y-%m-%d')]['Close'].values
    period_start_close = df.loc[df['Date'] == period_start.strftime('%Y-%m-%d')]['Close'].values
    prev_day_volume = df.loc[df['Date'] == prev_day.strftime('%Y-%m-%d')]['Volume'].values

    # check if date is not in the dataframe
    if len(prev_day_close) == 0 or len(period_start_close) == 0 or len(prev_day_volume) == 0:
        return None

    factor = ((prev_day_close - period_start_close) / period_start_close) / prev_day_volume * 100

    # check if factor is NaN
    if pd.isnull(factor).any():
        return None
    
    return factor


if __name__ == '__main__':
    combine_volume_adjusted_momentums('../../task_1/data')
