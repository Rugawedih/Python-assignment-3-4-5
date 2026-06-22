from sys import getsizeof

x = 21
num = 7.14
flag = True 

print ("The DataType is :",type(x))
print ("The Memory Address is :",id(x))
print("The Size in Bytes is :", getsizeof(x))

print ("The DataType is :",type(num))
print ("The Memory Address is :",id(num))
print("The Size in Bytes is :", getsizeof(num))

print ("The DataType is :",type(flag))
print ("The Memory Address is :",id(flag))
print("The Size in Bytes is :", getsizeof(flag))