# a) Write a Python script to check whether a given key already exists in a dictionary.

dect1={'t1':'item1','t2':'item2'}#define dictionary
key=input("enter key to check it is already exists in a dictionary? : ")
if key in dect1:
    print("key is already exist")
else:
    print("key is not present")

# b) Write a Python script to merge two Python dictionaries.
dect2={'t1':'item1','t2':'item2'}
dect3={'h3':'item3','h4':'item4'}
dect2.update(dect3) #for merge two dictionaries
print(dect2)

# c) Write a Python program to sum all the items in a dictionary.
dect4={0:100,1:101,2:102,3:103}
print(sum(dect4.values())) #sum of all the values of dictionary

# d) Write a Python script to add a key to a dictionary.
dect5={0:'zero',1:'one'}
dect5.update({2:'two'}) #adding element
print(dect5)

# e) Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}

for i in [dic1,dic2,dic3]:
    dic4.update(i)

print(dic4)

