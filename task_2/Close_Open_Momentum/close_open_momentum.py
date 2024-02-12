from datetime import datetime, timedelta
import os
import pandas as pd


def combine_close_open_momentums(path):
    close_open_momentum_df = pd.DataFrame()

    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(path, filename))
            df = df[['Date', 'Close', 'Open']]

            temp_ticker_df = pd.DataFrame()
            temp_ticker_df['Date'] = df['Date']
            ticker_name = filename.split('.')[0]
            temp_ticker_df[ticker_name] = None

            for index, row in df.iterrows():
                date = row['Date']
                close_open_momentum = calculate_close_open_momentum(date, df)
                temp_ticker_df.at[index, ticker_name] = close_open_momentum

            if close_open_momentum_df.empty:
                close_open_momentum_df = temp_ticker_df
            else:
                close_open_momentum_df = pd.merge(close_open_momentum_df, temp_ticker_df, on='Date', how='inner')

    close_open_momentum_df.set_index('Date', inplace=True)
    close_open_momentum_df.to_csv('close_open_momentum.csv')


def calculate_close_open_momentum(date, df):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')

    prev_day = datetime_obj - timedelta(days=1)

    prev_day_close = df.loc[df['Date'] == prev_day.strftime('%Y-%m-%d')]['Close'].values
    today_open = df.loc[df['Date'] == date]['Open'].values

    # check if date is not in the dataframe
    if len(prev_day_close) == 0 or len(today_open) == 0:
        return None

    factor = 100 * (today_open - prev_day_close) / prev_day_close

    # check if factor is NaN
    if pd.isnull(factor).any():
        return None
    
    return factor


if __name__ == '__main__':
    combine_close_open_momentums('../../task_1/data')
