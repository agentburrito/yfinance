## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1

# System Test Case:

# Different Class Symbol Download

```
Purpose: Testing full parameter download function for tickers with different classes
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
1    | Input BRK.A symbol| Historical stock  | Symbol not found | Fail
     | and get full      | data              |                  |
     | download data     |                   |                  |
----------------------------------------------------------------------------
2    | Input BRK-A symbol| Historical stock  | Historical stock | Pass
     | and get full      | data              | data             |
     | download data     |                   |                  |
----------------------------------------------------------------------------
```
