import torch

x = torch.ones(3,3)
x*=-1
print(x)
print(torch.abs(x))