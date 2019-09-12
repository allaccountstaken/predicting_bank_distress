# US Banks Distress Early Warning  System
## This classification is based on machine learning of distress features captured by CALL reports

### Number of failing banks increased sharply in 2009-2012 what gave hope of modeling these rare events
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Hist%20number%20of%20failed%20banks.png)

### CAMELS framework was used for building risk profiles. Healthy bank will not exceed risk capacity:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Healthy%20bank%20CAMELS%20profile.png)

### Failing bank will likely exceed capacity along Assets, Earnings, and Liquidity risk dimensions:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Failed%20bank%20CAMELS%20profile.png)

### Various models were trained and compared based on their recall scores:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Insample%20recall%20scores.png)

### Logistic regression performed best out of sample with high and stable prediction recall scores for the next 9 quarters:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Outofsample_recall.png)

## Also in this repository you will find:
1) Selected financials provided by healthy banks as of 2010-Q3
2) Selected financials provided by failed banks as of 2010-Q3
3) CAMELS dimensions calculated from these selected financials
4) CAMELS time series data from 2009-Q4 to 2010-Q3
5) Validation datasets from 2010-Q4 to 2012Q4
6) Python client to connect to SOAP server and pull more data
7) basic_model used on raw data before over-sampling with SMOTE
8) PDF file with CALL report example
9) custom_functions.py file with some additional functions 

