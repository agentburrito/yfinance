## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1


# TEST CASE REPORT

# Testing full parameter download function for tickers with different classes

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
Test if full parameter download works for symbols with different classes using BRK.A and BRK-A
```
Results:  ``pass`` 
### INTRODUCTION
Set Up Procedures: 
```
Get download data for full parameters inputted in function for all symbols in dataset
```
Stop Procedures:
```
Either receive error or get all rows for every symbol
```
### TEST
Test Items and Features: 
```
Items: BRK.A BRK-A
```
```
Features: Gets download data
```
Input Specifications: 
```
"BRK-A"
"BRK.A"
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
replace symbols with "BRK.A" and "BRK-A" as needed
```
Expected Results of Case:
```
All rows should be non empty
```
### ACTUAL RESULTS
BRK.A
Output Specifications: ``Fail``
```
1 Failed download:
- BRK.A: No data found, symbol may be delisted
Empty DataFrame
Columns: [Open, High, Low, Close, Adj Close, Volume]
Index: []

```
BRK-A
Output Specifications: ``Pass``
```
                Open      High       Low  ...  Volume  Dividends  Stock Splits
Date                                      ...
2020-01-28  335600.0  338000.0  335032.0  ...       2          0             0
2020-01-29  336250.0  339400.0  336250.0  ...       1          0             0
2020-01-30  334360.0  342000.0  334360.0  ...       2          0             0
2020-01-31  339855.0  339855.0  335120.0  ...       3          0             0
2020-02-03  338160.0  339450.0  334580.0  ...       2          0             0
...              ...       ...       ...  ...     ...        ...           ...
2021-01-29  344749.0  346355.0  343000.0  ...       3          0             0
2021-02-01  345000.0  346945.0  344250.0  ...       3          0             0
2021-02-02  348300.0  352000.0  348300.0  ...       4          0             0
2021-02-03  350200.0  351086.0  349250.0  ...       2          0             0
2021-02-04  351700.0  355000.0  351192.0  ...       4          0             0

[259 rows x 7 columns]
```