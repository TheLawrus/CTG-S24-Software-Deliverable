## Installation

Install pandas and Yahoo Finance API from requirements.txt

## Usage

- Tickers to be retrieved are newline separated in `tickers.txt`
- Using yfinance, the following are retrieved for each ticker in the time range 01/01/2021 to 12/31/2023:
  - Date
  - Open
  - High
  - Low
  - Close
  - Volume
  - Adjusted Close
- The data for each ticker is saved as a CSV file in `data/` such that each row is a date containing the above data for that day
- For days where the market was closed, I filled in the previous day's valiues to ensure that dates were continuous in the CSV file

## Issues Encountered

- Pandas has a deprecation warning related to the yf.download() function. Since this needs to be resolved by the yfinance package, I have suppressed the warning.
