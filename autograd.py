import torch

#Autograd example using a simple neural network 
#OJO: autograd == backpropagation

#4 different tensors
x = torch.randn(1,10) #input
prev_h = torch.randn(1,20) #hidden state of the RNN that gives it its memory
W_h = torch.randn(20,20) #learning weights for the hidden state
W_x = torch.randn(20,10) #learning weights for the input

i2h = torch.mm(W_x, x.t()) #multiply the weights by their respective tensors. mm stands for "matrix multiplication"
h2h = torch.mm(W_h, prev_h.t()) #multiply the weights by their respective tensors. mm stands for "matrix multiplication"
next_h = i2h + h2h #add the outputs of the 2 matrix multiplications
next_h = next_h.tanh() #pass the result thru an activation fxn

loss = next_h.sum() #compute the loss. The loss is the difference between the correct output and the actual prediction of our model.
loss.backward() #backpropagation aka autograd 