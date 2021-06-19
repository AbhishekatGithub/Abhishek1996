           Data

Weather data of temperature, humidity and rainfall of Kanto region in USA( all values standardized in same scale of SI units)

          Approach

Multinomial linear regression in PyTorch using gradient descent optimization. Estimated the yield of crops 1 and 2 as a plane in 3D space obtained by a linear combination of parameters plus the biases

          Method

Weights and biases are estimated using random sampling and Torch optimization function (torch.SGD.optim) after 100 epochs to arrive at the best values for the best fit plane.

         Evaluation

Plots of target values obtained vs real values from randomly sampled test values
R square values 
