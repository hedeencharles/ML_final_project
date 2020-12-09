# Health Care Analytics

## First dataset: Cancer Level Data set
* The objective for this data set was to build a machine learning model to accurately predict the level of severity of Cancer based on a set of 23 features.

* The conclusion, after attempting to build machine learning models and analyzing the models and data more thoroughly, was that the dataset was suspect, as all models resulted in 100% accuracy, a situation that results in Overfitting.  
* The process the team followed and the analysis steps and conclusion are documented in a Tableau workbook that can be found [here.](https://public.tableau.com/profile/paul.hardy#!/vizhome/CancerStudyDataAnalysis/STORY-TheLungCancerLevelDataset?publish=yes)

## Dataset source:
* The source of the Cancer Dataset is [here.](https://www.kaggle.com/rishidamarla/cancer-patients-data)

---

## Second dataset: Health Insurance cost
## Objective
* Build a machine learning model that can accurately predict an individual's yearly health insurance charges, based on the following:
  * Model's features (individuals information) will consist of:
      1. Age
      2. Number of children on plan
      3. BMI (body mass index)
      4. Gender
      5. Smoker(y/n)
      6. Region (Southwest, Southeast, Northwest and Northeast)
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
      * Although the Random Forest did not produce the overall highest accuracy, from what we know about the regressions tested, Random Forest will perform better when given outliers and values that are not within the SVR's insensitive tube. 
      * Random Forest will also provide insight into what features have the most importance to the model's predictions. From the feature importance module, we discovered the model is heavily dependent on an individual's BMI and number of children on the plan. 
      * Because our model is heavily dependent on BMI and number of children, the model struggles to predict insurance cost for individuals with a very low/high BMI and no children. 

## Flask App
  * Loads the Random Forest model at the beginning 
    * This helps with performance for the webpage prediction
  * Receives inputs from the webpage
  * Through the predict_model function, the inputs are compiled into one array, encoded and passed into the model
  * The model runs and outputs the health insurance cost prediction based on those passed in inputs.
  * The model's prediction is then passed back to the webpage to be displayed.

## Dataset source:
* Insurance: https://www.kaggle.com/mirichoi0218/insurance