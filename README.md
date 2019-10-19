# Bank Distress Early Warning System
## This project aims to predict out-of-sample financial distress of US banks one quarter prior to their failure with maximum accuracy defined as recall score (TP/P). Predictions will be based on machine learning of distress features that are possibly captured by  app. 25,000 quarterly financial reports (FDIC CALL reports). Logistic regression was found to work best for out-of-sample forecast.

#### In normal, non-stressed environment it is very hard to predict failing banks as they are very rare, i.e. anomaly, and hence one needs to create a profile, or a standard,  of a "normal" bank:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Healthy%20and%20Failed%20banks.png)

#### Number of failing banks increased sharply in 2009-2012 what allowed training models on real data with SMOTE sampling:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Hist%20number%20of%20failed%20banks.png)

#### CAMELS framework was used for building banks' profiles. Healthy bank will not exceed risk capacity:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Healthy%20bank%20CAMELS%20profile.png)

#### Failing bank will likely exceed capacity along Assets, Earnings, and Liquidity risk dimensions:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Failed%20bank%20CAMELS%20profile.png)

#### Various models were trained and compared based on their recall scores:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Insample%20recall%20scores.png)

#### Logistic regression performed best on out-of-sample data with high and stable recall scores for the next 9 quarters:
![](https://github.com/allaccountstaken/predicting_bank_distress/blob/master/images/Outofsample_recall.png)

## Also in this repository you will find:
1) Selected financials provided by healthy banks as of 2010-Q3
2) Selected financials provided by failed banks as of 2010-Q3
3) CAMELS dimensions calculated from these selected financials
4) CAMELS time series data from 2009-Q4 to 2010-Q3
5) Validation datasets from 2010-Q4 to 2012-Q4
6) Python client to connect to SOAP server and pull banks' data
7) Deck of slides that gives a brief presentation of this research
8) PDF file with CALL report example
9) custom_functions.py file with some additional functions 

