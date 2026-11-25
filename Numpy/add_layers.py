import numpy as np
M=np.array([[1,2,3],
           [2,3,4]])
print(M)
print(M.shape)

V=np.array([2,3,2])
print(V.shape)

multiply=M@V
print(multiply)
print(multiply.shape)


x = np.array([0.5, 1.2, -0.3])         # inputs 
W = np.array([[0.4, -0.6, 0.9],        # neuron 1
              [0.2,  0.8, -0.5],       # neuron 2
              [-0.7, 0.1, 0.3]])       # neuron 3
b = np.array([0.1, 0.0, -0.2])         # one bias per neuron

z= (W@x) +  b
print(z)

def sigmoid(z):
    return 1/(1+np.exp(-z))

output=sigmoid(z)
print(output)
