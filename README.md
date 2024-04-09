# Loan-Approval-Predictor


### Project Overview

This data analysis project aims to make a loan approval predictor rest attributes present in the dataset and analyze what features/attributes play a key role in approval or rejection of loan.


### Data Sources

The dataset used is obtained from Kaggle website.
The dataset consists of 614 entries having 13 columns, namely-
User id, gender, education, loan amount, loan amount term, married, self employed, credit history, dependents, applicant income, co-applicant income, property area and loan status.


### Tools

- Google Colab


### ML algorithm

- Random Forest 


### Data Cleaning/Preparation
In the initial data preparation phase, we performed the following tasks:
1. Data loading and inspection.
2. After analysing, we know, that there are categorical data and some missing values in the dataset.Thus, we’ll be using label encoder for multiple columns and one-hot ‘Property-Area’(3 unique values) column.
3. Handling missing values by replacing them with most used values in the particular column
4. And then perform feature scaling before fitting the ML algorithm.


### Exploratory Data Analysis

EDA involved exploring the dataset to answer key questions, such as:- What is the overall loan approval rate?
- What is the loan approval distribution for males and females? and similarly for unmarried and married applicants?
- Does dependencies have any impact on loan approval?
- What role does credit history play?


### Data Analysis

First, we split the dataset into the Training set and Test set and then fitting the Random Forest Classification to the Training set.
Then use the Random Forest Classifier to predict for both train and test data
Also check for performance metrics for both the training and testing data


### Results/Findings

The loan predictor model is thus built. We got accuracy of 79% which is fairly good.And also the wrong predictions are 25 out of 183 predictions. This is the lowest we got using RF model with estimators 55 for this dataset. Some important findings are -
- We can see, that the married applicants are more than the unmarried applicants ; also, there are very few female applicants.
- For this particular dataset , mostly loans are approved, and less than 50% are rejected- Loan approval chances are more for Semiurban property applicants, then urban, and finally rural.
- Credit history surely plays a very vital role, and better the credit score history, more loan approval chances
- Graduates are more likely to get loan
- The less the no. of dependencies on the applicant, chances of loan approval are more


### Recommendations

- Improve your credit score history.
- Choose your property area wisely,as its comparatively easy to get loans for semiurban area than urban and then rural.
- Education helps, as graduates stand more chance in getting loans.
