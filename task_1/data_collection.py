import pandas as pd
import yfinance as yf
import warnings

# used to suppress FutureWarning related to yf.download()
warnings.filterwarnings("ignore", category=FutureWarning, module="yfinance")

def get_data():
    # get tickers from tickers.txt
    tickers = []
    with open('tickers.txt', 'r') as file:
        tickers = file.read().splitlines()

    # for each ticker get data and save to csv
    for ticker in tickers:
        data = yf.download(ticker, start="2021-01-01", end="2023-12-31", keepna=True)

        data = pd.DataFrame(data)

        # check for null values
        if data.isnull().values.any():
            print(f'{ticker} has null values')
            data = data.fillna(method='ffill')

        # fill in missing dates
        idx = pd.date_range('2021-01-01', '2023-12-31')
        data.index = pd.DatetimeIndex(data.index)
        data = data.reindex(idx, method='ffill')
        data.index.rename('Date', inplace=True)

        # ensure each ticker has the same number of data points
        if len(data) != 1095:
            print(f'{ticker} has {len(data)} data points')
            continue

        data.to_csv(f'data/{ticker}.csv')


if __name__ == '__main__':
    get_data()
