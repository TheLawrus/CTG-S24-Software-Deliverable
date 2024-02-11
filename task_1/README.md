## Intallation

Install pandas and Yahoo Finance API from requirements.txt

## Usage

- Tickers to be retrieved are newline separated in `tickers.txt`
- Using yfinance, the following are retrieved for each ticker: Date, Open, High, Low, Close, Volume, and Adjusted Close in the time range 01/01/2021 to 12/31/2023
- The data for each ticker is saved as a CSV file in `data/` such that each row corresponds to each date containing the above data

## Issues Encountered

- Pandas has a deprecation warning related to the yf.download() function. Since this needs to be resolved by the yfinance package, I have suppressed the warning.
