# a) Write a Python program to add member(s) in a set and clear a set

s1=set() #empty set
s1.add('apple')
# s1.add({0:1})
# s1.add([2,3])
s1.add(('h','s'))
print(s1)
s1.clear() #to clear a set
print(s1)

# b) Write a Python program to remove an item from a set if it is present in the set.

s2={1,2,3,4,5,6,7}
s2.discard(5) # for remove specific element
print(s2)

# c) Write a Python program to create an intersection, Union, difference of sets.

natural_num={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
odd_num={1,3,5,7,9}

print(natural_num.union(odd_num)) # for union
print(natural_num.intersection(odd_num)) # for intersection
print(natural_num.difference(odd_num)) # for difference

# d) Write a Python program to find maximum and the minimum value in a set.

s3={11,9,4,22,7,33,11}
print(max(s3)) # for maximum value
print(min(s3)) # for minimum value

# e) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
s4 = [1, 1, 2]
most_common = max(s4, key = s4.count) # for most common element
a=most_common
counter=s4.count(a) # most common element counter
print(counter)
print(most_common)

