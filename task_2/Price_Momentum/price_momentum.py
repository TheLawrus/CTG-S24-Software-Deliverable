from datetime import datetime, timedelta
import os
import pandas as pd


def combine_price_momentums(path):
    price_momentum_df = pd.DataFrame()

    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(path, filename))
            df = df[['Date', 'Close']]

            temp_ticker_df = pd.DataFrame()
            temp_ticker_df['Date'] = df['Date']
            ticker_name = filename.split('.')[0]
            temp_ticker_df[ticker_name] = None

            for index, row in df.iterrows():
                date = row['Date']
                price_momentum = calculate_price_momentum(date, df)
                temp_ticker_df.at[index, ticker_name] = price_momentum

            if price_momentum_df.empty:
                price_momentum_df = temp_ticker_df
            else:
                price_momentum_df = pd.merge(price_momentum_df, temp_ticker_df, on='Date', how='inner')

    price_momentum_df.set_index('Date', inplace=True)
    price_momentum_df.to_csv('price_momentum.csv')


def calculate_price_momentum(date, df):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d')

    prev_day = datetime_obj - timedelta(days=1)
    period_start = prev_day - timedelta(days=5)

    prev_day_close = df.loc[df['Date'] == prev_day.strftime('%Y-%m-%d')]['Close'].values
    period_start_close = df.loc[df['Date'] == period_start.strftime('%Y-%m-%d')]['Close'].values

    # check if date is not in the dataframe
    if len(prev_day_close) == 0 or len(period_start_close) == 0:
        return None

    factor = ((prev_day_close - period_start_close) / period_start_close) * 100

    # check if factor is NaN
    if pd.isnull(factor).any():
        return None
    
    return factor


if __name__ == '__main__':
    combine_price_momentums('../../task_1/data')
