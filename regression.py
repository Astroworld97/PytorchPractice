import numpy as np


#model: y = a + bx + epsilon
#Note: a=1, b=2
#obtained from: https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e

#data generation

np.random.seed(42)
x = np.random.rand(100, 1)
y = 1 + 2 * x + .1 * np.random.randn(100,1)