## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1


# TEST CASE REPORT

# Testing hang on massive dataset download

### GENERAL INFORMATION

Test Stage: 
```
Unit Test
```
Test Date: 
```
2021-03-26
```
Tester: 
```
Max Melendez
```
Test Case Description:
```
Test if download hangs when attempting to download data for a big dataset at the same time
```
Results:  ``pass`` 
### INTRODUCTION
Set Up Procedures: 
```
Get download data for full parameters inputted in function for all symbols in dataset
```
Stop Procedures:
```
Either download completes or the function hangs
```
### TEST
Test Items and Features: 
```
Items: Using nyse_data.txt that contains a list of over 6000 symbols listed in the New York Stock Exchange
```
```
Features: Gets download data
```
Input Specifications: 
```
split test data using /n as follows: 

testdata = open("nyse_data.txt","r")
symbols = testdata.read()
symbols = symbols.split("\n")

```
Procedural Steps: 
```
Execute download using following parameters and print data:

data = yf.download(
        tickers = symbols,

        period = "ytd",

        interval = "1d",

        start="2020-01-28", 
        
        end="2021-02-05",

        group_by = 'ticker',

        auto_adjust = True,

        prepost = True,

        threads = True,

        proxy = None,

        actions = True,

        rounding = True
    )
```
Expected Results of Case:
```
Download completes
```
### ACTUAL RESULTS
nyse_data.txt
Output Specifications: ``Pass``
```
[*********************100%***********************]  6666 of 6666 completed
913 Failed downloads:
- SHQA: No data found, symbol may be delisted
- WPCB: No data found, symbol may be delisted
- IMMU: No data found, symbol may be delisted
- THCP: No data found, symbol may be delisted
.
.
.
- ATMR: No data found for this date range, symbol may be delisted
- SRNG: No data found for this date range, symbol may be delisted

           SHQA                 ...    UHAL
           Open High Low Close  ...   Close   Volume Dividends Stock Splits
Date                            ...
2020-01-28  NaN  NaN NaN   NaN  ...  369.26  27300.0       0.0          0.0
2020-01-29  NaN  NaN NaN   NaN  ...  369.31  32200.0       0.0          0.0
2020-01-30  NaN  NaN NaN   NaN  ...  368.70  43700.0       0.0          0.0
2020-01-31  NaN  NaN NaN   NaN  ...  369.12  61400.0       0.0          0.0
2020-02-03  NaN  NaN NaN   NaN  ...  361.94  70200.0       0.0          0.0
...         ...  ...  ..   ...  ...     ...      ...       ...          ...
2021-02-01  NaN  NaN NaN   NaN  ...  476.33  47200.0       0.0          0.0
2021-02-02  NaN  NaN NaN   NaN  ...  477.20  40100.0       0.0          0.0
2021-02-03  NaN  NaN NaN   NaN  ...  482.02  47800.0       0.0          0.0
2021-02-04  NaN  NaN NaN   NaN  ...  495.63  69800.0       0.0          0.0
2021-02-05  NaN  NaN NaN   NaN  ...     NaN      NaN       NaN          NaN

[263 rows x 45749 columns]
```