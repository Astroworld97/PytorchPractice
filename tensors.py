#The simplest way to create a tensor is with the torch.empty() function.
#Remember, PyTorch follows the (r,c) nomenclature for indexing: (rows, columns)
import torch

x = torch.empty(3,4) #3 rows, 4 columns
print(type(x))
print(x)
