**Application Demo**




https://user-images.githubusercontent.com/79574776/126908434-ad6b0473-310d-4b53-836c-490b6a35f264.mp4




Deployed a house price prediction streamlit app on Heroku, which not only predicts price but also shows their locations on a map. 

Assumption: Price of property did not vary after the dataset was released in 2014 by USA surveys.

          Parameters/ features used for prediciting price:

  * Number of bedrooms - Categorical variable
  * Space required in sq.feet - Continuous variable
  * Number of bathrooms  - Ordinal variable
  * Number of floors - Categorical variable
  * Waterfront or not - Binary categorical variable


        Algorithms


Pipeline of DecisionTree, RandomForest, GradientBoosting and Linear Regression models.Selected the model based on the RMSE value, varies depending upon each run and user inputs.
Coordinates mapped into map using zipcodes vs lat-lon dataset from USA survey 2014. 


         Output

* Price: Prediction based on four regression models 1) DecisionTree 2) RandomForest 3) Gradient Bosting Tree 4) Linear regression
* Map: The property is located by mappping coordinates from zip codes available in the database( via API, which does not exist now!)

       Evaluation criteria - RMSE(Root mean square error) minimization

Git : https://github.com/AbhishekatGithub/houseprices_streamlit


App Link: https://usa-house-price-location.herokuapp.com/
