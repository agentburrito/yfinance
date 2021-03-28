## ACKNOWLEDGEMENTS
This markdown file template was kindly provided to me by maazs1



# Test Plan
## 1 Introduction

The test plan is created to communicate the test approach to team members. It includes the objectives,
task assignments, problems found during the research phase, risks, severity of source code to be tested,
test approach, and test environment.

### 1.1 Objective

To test the functionality of download in multi.py and identify critical failures and areas of concern.


### 1.2 Team Members and Host Repo
Max Melendez, mmelende https://github.com/agentburrito/
https://github.com/agentburrito/yfinance
## 2 Problems Found

a). Downloads can sometimes hang when attempting to download many tickers at once

b.) The format of certain tickers (different class tickers) can result in issues downloading. For example attempting to download a class A ticker using symbol.A will result in an error.

c.) NaN  last row when downloading large amounts of data. 


## 3 List of Planned Tests


a). Test if full parameter download with entire dataset works

b). Test if downloading different class tickers works

c). Test if all rows are present when downloading multiple ticker data at once

## 4 Risks Involved

```#                   Risk                                           Impact                Trigger                    Mitigation Plan```
```
1. Limited Resources
Due to an absolute lack of communication by my group, I must undertake a lot of work by myself. This will limit the quality and breadth of the work I can produce in a limited amount of time for the amount of work (1-3 hours) specified by the assignment.
```
```
2. Changes to the functionality may negate the tests already written and may result in a loss of test cases already written
```
```
3 Some test may not pass due to unfixable or difficult to fix errors.
```
## 5 Test Approach

```
I created a dataset containing over 6000 NYSE symbols to stress test the download capabilites of the program. This will form the basis of all tests I run
```
## 6 Test Environment

```
App should run under the following environment:
              python>= 2.7, 3.4+ with multitasking and yfinancemodule installed
```
