               Problem Statement


Multiclass classification of E-commerce products into four classes 1 through 4 of 0.1 M products/records with 48 categorical features of which most of them are right skewed.
The objective is to predict the classes and return the probability of occurannce for each class for all the products( test data with 50k records)


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
  LightGBM was better both on scores and speed, a good choice for this sparsely located dataset values with more categorical features spread over a large range(-10 to 75) 
  OPTUNA --> Used for hyper-parameter optimization with 20 trials, best result with LGBM of 1.087 log-loss score
  
         Evaluation criteria
  
  Log-Loss score : 1.087 , which placed the model on the top 25% of all models in Kaggle
  
        Key insights
  
  Not in all cases is 1) removing outliers and 2) random upsampling of minor classes for dealing with imbalanced classes yield a better result 3) Each model has its own advangtages for a particular typr of dataset and its category 4) Domain kknowledge has to be applied for feature engineering, failing to have a good grasp on domain can be supplemented with careful analysis of all features and considering all as equally important and proceeding further from there.
