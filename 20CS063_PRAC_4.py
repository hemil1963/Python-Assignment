''' ID:-20CS063    NAME:Hemil Patoliya'''
'''AIM:- Find runner-up from given list'''
n = int(input()) #length of numbers
arr = map(int, input().split())
arr = list(set(list(arr))) #converted in list
length = len(arr)
arr = sorted(arr) #sorted list
print(arr[length-2])