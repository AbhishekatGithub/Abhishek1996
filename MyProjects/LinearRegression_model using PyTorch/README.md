           Objective
           
   Predict the yield of two crops based on the given parameters using Pytorch, multiple regression with stochastic gradient descent 
           
           Data

Weather data of temperature, humidity and rainfall of Kanto region in USA( all values standardized in same scale of SI units)

          Approach

Multinomial linear regression in PyTorch using gradient descent optimization. Estimated the yield of crops 1 and 2 as a plane in 3D space obtained by a linear combination of parameters plus the biases

          Method

Weights and biases are estimated using random sampling and Torch optimization function (torch.SGD.optim) after 100 epochs to arrive at the best values for the best fit plane.

         Evaluation

Plots of target values obtained vs real values from randomly sampled test values and R square values 



![a1](https://user-images.githubusercontent.com/79574776/126943840-53f163bb-7968-4aab-a243-6dc6bee9c4d8.png)


![a2](https://user-images.githubusercontent.com/79574776/126943854-ce72b52a-378c-460d-a341-14e72be7e78c.png)
