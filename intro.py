import torch

z = torch.zeros(5, 3) #creates a tensor with 5 rows and 3 columns and fills it with zeros
print(z)
print(z.dtype) #prints out the datatype contained. The default is 32-bit floating point numbers.

i = torch.ones((5,3), dtype=torch.int16) #changes the datatype from floats to ints
print(i)
print(i.dtype)

torch.manual_seed(1729) #a seed for the random number generator
r1 = torch.rand(2,2)
print('A random tensor: ')
print(r1)