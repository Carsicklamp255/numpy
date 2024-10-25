import numpy as np

lista_normal = [5, 3.6, 2, 8, 9]
array = np.array(lista_normal, dtype = int)
print(lista_normal)

print(array)
print(type(array))
print(array.dtype)

#dimensions

ar1 = np.array


ar4 = np.array([[
    [1,2,3]
    [4,5,6]
],
[
    [1,2,3]
    [4,5,6]

]])
print(ar4)
print(ar4.ndim)

arr = np.array()
print(arr)
print(arr[1,2])

arr = np.array([[[1,2,3], [4,5,6], [7,8,9],[10,11,12]]])

print(arr[1,-1,1])

#slicing
lista = np.arrange(15)
print(lista)

pedaco = lista[5:9]
print(pedaco)

pedaco[0] = 69
print(pedaco)
print(lista)

#data types

frutas = np.array('banan', 'maça', 'morango', 'laranja')
print(frutas)
print(frutas.dtype)

numeros = np.array([1,2,3,4], dtype='f8')
print(numeros)
print(numeros.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype