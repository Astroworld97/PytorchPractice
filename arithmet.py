import torch

ones = torch.ones(2,3)
print(ones)

twos = torch.ones(2,3) * 2 #every element is multiplied by 2
print(twos)

threes = ones + twos #addition allowed bc shapes are similar
print(threes) #tensors are added element-wise
print(threes.shape) #this has the same dimensions as input tensors

# Arithmetic below fails due to the tensors being of different dimensions
# r1 = torch.rand(2,3)
# r2 = torch.rand(3,2)
# r3 = r1 + r2