# Credit Risk Scorecard Analysis

For details, please check the report [HERE](https://github.com/yovalishere/Finance/blob/main/Credit%20Risk%20Scorecard%20Analysis/CreditRisk_Report.pdf)
### Project description
This project focuses on behavioural credit risk scorecard analysis. 5 classification models were
used for prediction performance comparison. They are :
1) Logistics Regression
2) Support Vector Machine (SVM)
3) Decision tree
4) Random Forest 
5) XGBoost

### Data description
The dataset is a record of customer default payment in Taiwan in October 2005. It is retrieved from [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).
It consists of 30,000 rows of data. There are 24 variables in total which correspond to 23 
dependent variables and 1 independent variable.

### Project findings
**PAY_1** (payment delay for 1 month) and **PAY_2** (payment delay for 2 months) are the most important features found by the optimal model.
<img src="https://github.com/yovalishere/Finance/blob/main/Credit%20Risk%20Scorecard%20Analysis/Feature%20importance%20from%20Random%20Forest.jpg" width="450" height="350" /><br>

**Random forest model after hyperparameter tuning** gives the best result.<br><br>
<img src="https://github.com/yovalishere/Finance/blob/main/Credit%20Risk%20Scorecard%20Analysis/Summary%20statistics%20for%20model%20performance.jpg" width="450" height="350" />

