## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1

# System Test Case:

# Full Parameter Download Test

```
Purpose: Testing full parameter download function with a single symbol as well as with a massive dataset.
```
```
Test Run Info:
Tester Name: Max Melendez
Date(s) of Test: 2021-03-26
```
```
TEST SCRIPT STEPS/RESULT:

STEP | TEST STEP/INPUT   |  EXPECTED RESULT  |  ACTUAL RESULTS  | PASS/FAIL
----------------------------------------------------------------------------
1    | Input MSFT symbol | Historical stock  | Historical stock | Pass
     | and get full      | data              | data             |
     | download data     |                   |                  |
----------------------------------------------------------------------------
2    | Input             | Historical stock  | Empty data       | Fail
     | nyse_data.txt data| data              |                  |
     | and get full      |                   |                  |
     | download data     |                   |                  |
----------------------------------------------------------------------------
```
