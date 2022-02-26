''' ID:-20CS063    NAME:Hemil Patoliya'''
'''AIM:- Lapindrome'''

n = int(input())

for i in range(n):
    k = input()
    l = len(k)
    if l % 2 == 0:
        x = k[:int(l/2)] 
        y= k[int(l/2):] # for l's length even 
    else:
        x= k[:int(l/2)]
        y= k[int(l/2)+1:] # for l's length odd
    if sorted(x) == sorted(y): #sorting and compare
        print("YES")
    else:
        print("NO")