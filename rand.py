import torch

torch.manual_seed(1729) #a seed for the random number generator
r1 = torch.rand(2,2)
print('A random tensor: ')
print(r1)

r2 = torch.rand(2,2)
print("\nA different random tensor: ")
print(r2)

torch.manual_seed(1729)
r3 = torch.rand(2,2)
print("\nShould match r1: ")
print(r3) #repeats values of r1 because of reseeding
