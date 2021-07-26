               Problem Statement


Multiclass classification of E-commerce products into four classes 1 through 4 of 0.1 M products/records with 48 categorical features of which most of them are right skewed.
The objective is to predict the classes and return the probability of occurance for each class for all the products( test data with 50k records)


              Data

Training : 0.1 M records with 48 categorical and some semi-ordinal features and four classes 

Testing  : 50K records to be classified into these four classes as a measure of its probabality to be in that class


            Approach / Feature engineering

  * Exploratory data analysis of training data with seaborn and Pandas
  * Stripplot, boxplot, barplots to explore the categories of features and its nature
  * SMOTE analysis experimentation for highly imbalanced classes( Class II occured predominantly)---> did not yield positive results
  * Outliers were unable to be defined with lot of unique categorical features which were spread----> outlier treatment with z-score and IQR did not work as outliers were not   obvious and were required for useful information.
  * Negative values played a role in correct identiification with better log-loss score
  
             Methods and Models
  
  Random Forest , XGBoost and LightGBM were used in a pipeline 
  **LightGBM** was better both on scores and speed, a good choice for this sparsely located dataset values with more categorical features spread over a large range(-10 to 75) 
  
  **OPTUNA** --> Used for hyper-parameter optimization with 20 trials, best result with LGBM of 1.087 log-loss score
  
         Evaluation criteria
  
  Log-Loss score : 1.087 , which placed the model on the top 25% of all models in Kaggle
  
        Key insights
  
  Not in all cases is 1) removing outliers and 2) random upsampling of minor classes for dealing with imbalanced classes yield a better result 3) Each model has its own advangtages for a particular type of dataset and its category 4) Domain knowledge has to be applied for feature engineering, failing to have a good grasp on domain can be supplemented with careful analysis of all features and considering all as equally important and proceeding further from there.




### **Overview of the Project, see notebook for details and the code**

**Imbalanced classes**

SMOTE analysis, Over/Undersampling techniques

![t1](https://user-images.githubusercontent.com/79574776/127012022-7a64c13d-72b8-4119-89d6-362b86d9781b.png)

Stripplot of the entire dataset > We can visualize outlying values, comapred to the normal distribution as seen below

![t2](https://user-images.githubusercontent.com/79574776/127012031-239cb9bd-203d-4ffe-805f-24e2111e6574.png)

**OPTUNA optimisation plots**

![t3](https://user-images.githubusercontent.com/79574776/127012005-1d247620-6bc5-43bf-a838-91dda6d00f82.png)

![t4](https://user-images.githubusercontent.com/79574776/127012017-47fceb20-6c86-4387-9343-3455e4bb6913.png)


BEST HYPER-PARAMETERS FOUND OUT BY TRIALS USING OPTUNA

![t5](https://user-images.githubusercontent.com/79574776/127012020-98ab5379-421b-447e-8a99-6b7d5ee06a0a.png)


