Deployed a house price prediction streamlit app on Heroku, which not only predicts price but also shows their locations on a map. 

Assumption: Price of property did not vary after the dataset was released in 2014 by USA surveys.

Parameters/ features used for prediciting price:

  * Number of bedrooms - Categorical variable
  * Space required in sq.feet - Continuous variable
  * Number of bathrooms  - Ordinal variable
  * Number of floors - Categorical variable
  * Waterfront or not - Binary categorical variable


Output

* Price: Prediction based on four regression models 1) DecisionTree 2) RandomForest 3) Gradient Bosting Tree 4) Linear regression
* Map: The property is located by mappping coordinates from zip codes available in the database( via API, which does not exist now!)

Evaluation criteria - RMSE(Root mean square error) minimization

Git : https://github.com/AbhishekatGithub/houseprices_streamlit


App Link: https://usa-house-price-location.herokuapp.com/
