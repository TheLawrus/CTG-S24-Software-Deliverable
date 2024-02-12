## Installation

Install pandas from requirements.txt

## Comments

- I called my custom factor _Close-Open Momentum_ where I calculate the difference in price from the previous day's close to the current day's open.
- In the provided `sample-factor.csv` file, only trading days are included, however, I opted to leave all dates in my factor CSV files because I think that is more useful to have.
- If it is desired to only include trading days in the factor CSV files, the steps to do that would be as follows:
  - add a function in task 1 to return the trading only dates from the Yahoo Finance API
  - call that function in task 2 and then drop all rows in the pandas dataframe that aren't in that list (i.e. dates that aren't in the trading days only list)
