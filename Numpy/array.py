import numpy as np 
a = np.array([1,3,5,7])
b = np.array([2,4,6,8])
print(a)
print(b)
print(a.shape)
print( a+b )
print( a*2 )
print( a*b )
print( np.dot(a,b) )
print( np.max(a) )
print( np.mean(a) )
print( np.sum(a) )
print( np.exp(a) )

#First neuron
x= np.array([1, 2, -0.3])
w= np.array([0, 0.5, 0.9])
b= 0.01
z= np.dot(x,w) + b
z=round(z,2)
print(z)
def sigmoid(z):
    return 1/(1+np.exp(-z))


output = round(sigmoid(z),2)
print(output)
layer0=sigmoid(np.array([-2, 0, 2]))
print(layer0)