# a) Write a Python program to create a tuple with different data types.

tpl1=('one',2,['a','b'],{0:100}) #define tuple
print(tpl1)

# b) Write a Python program to create a tuple with numbers and print one item.

tpl2=(1,2,3,4,5)
print(tpl2[3])

# c) Write a Python program to add an item in a tuple.

tpl3=('a','b','c','d')
tpl3=tpl3+('e',)#adding element in tuple
print(tpl3)

# d)  Write a Python program to convert a tuple to a string.

tpl4=('p','y','t','h','o','n')
s1="".join(tpl4) #convert tuple to string
print(s1)

# e) Write a Python program to find the length of a tuple.

tpl5=('h','e','m','i','l')
print(len(tpl5)) # for length of tuple