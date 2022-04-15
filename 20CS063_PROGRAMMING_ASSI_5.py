'''PREPARED BY-20CS063'''
try:
a = 10/0 print (a)
except ArithmeticError:
print ("This statement is raising an arithmetic exception.")
else:
print ("Success.")



###2)
try:
a = [1, 2, 3]
print (a[3]) except LookupError:
print ("Index out of bound error.")



###3)
class Attributes(object): pass

###4)
import math print(math.exp(1000))

##5)
array = [ 0, 1, 2 ] print (array[3])
