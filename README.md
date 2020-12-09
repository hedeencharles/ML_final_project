# ML_final_project

## Objective
* Build a machine learning model that can accurately predict an individuals yearly health insurance charges, based on the following:
  * Model's features (individuals information) will consist of:
      1) Age
      2) Number of children on plan
      3) BMI (body mass index)
      4) Gender
      5) Smoker(y/n)
      6) Region (Southwest, Southeast, Northwest and Northeast)
  * Analyze the dataset and visualize any interesting trends or phenomenon. 
    * Data exploration in Python Notebook to find possible correlations between features.
    * Import dataset into Tableau for visual analysis. 

## Machine Learning Models and Accuracy
  * Models Tested:
    * Decision Tree Regression (71.2% accurate)
    * Linear Regression (79.9% accurate)
    * Polynomial Regression (85.6% accurate)
    * Support Vector Regression (SVR) (88.7% accurate)
    * Random Forest Regression (88.2% accurate)
  * Model Used: 
    * Random Forest Regression!
      * Although the Random Forest did not produce the overall highest accuracy, from what we know about the regressions tested, Random Forest will perform better when given outliers and value that are not within the SVR's insensitive tube. 
      * Random Forest will also provide insight into what features have the most importance to the models predictions. From the feature importance module, we discovered the model is heavily dependent on an individuals BMI and number of children on the plan. 
      * Because our model is heavily dependent on BMI and number of children, the model struggles to predict insurance cost for individuals with a very low/high BMI and no children. 

## Flask App

## Dataset source:
* Insurance: https://www.kaggle.com/mirichoi0218/insurance