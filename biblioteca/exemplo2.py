import numpy as n

#shapes 
arr = n.array([[1,2,3], [4,5,6]])
print(arr)

print(arr.shape)

numeros = n.arange(15)
print(numeros)
numeros = numeros.reshape(3,5)
print(numeros)

numeros = n.arange(18)
print(numeros)
lm = numeros.reshape(2,3,3)
print(lm)