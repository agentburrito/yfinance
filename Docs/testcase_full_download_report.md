## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1


# TEST CASE REPORT

# Testing full parameter download function with a single symbol as well as with a massive dataset.

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
Test if full parameter download with custom dataset works as well as with a single ticker
```
Results:  ``pass`` 
### INTRODUCTION
Set Up Procedures: 
```
Get download data for full parameters inputted in function for all symbols in dataset
```
Stop Procedures:
```
Either receive empty data or get all rows for every symbol
```
### TEST
Test Items and Features: 
```
Items: Using nyse_data.txt that contains a list of over 6000 symbols listed in the New York Stock Exchange, single MSFT symbol
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
replace symbols with "MSFT" when testing single ticker.
```
Expected Results of Case:
```
All rows should be non empty and final output should be massive
```
### ACTUAL RESULTS
nyse_data.txt
Output Specifications: ``Fail``
```
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
MSFT
Output Specifications: ``Pass``
```
              Open    High     Low   Close    Volume  Dividends  Stock Splits
Date
2020-01-28  161.69  163.65  160.99  163.35  24899900        0.0             0
2020-01-29  165.70  166.60  163.58  165.90  34754500        0.0             0
2020-01-30  171.83  171.83  168.61  170.58  51597500        0.0             0
2020-01-31  170.01  170.20  167.42  168.06  36142700        0.0             0
2020-02-03  168.26  172.27  168.23  172.16  30149100        0.0             0
...            ...     ...     ...     ...       ...        ...           ...
2021-01-29  235.45  237.47  230.82  231.43  42503100        0.0             0
2021-02-01  234.52  241.94  231.90  239.10  33314200        0.0             0
2021-02-02  240.75  241.75  238.14  238.96  25916300        0.0             0
2021-02-03  239.02  244.53  238.71  242.44  27158100        0.0             0
2021-02-04  242.10  242.68  239.82  241.45  25296100        0.0             0

[259 rows x 7 columns]

```