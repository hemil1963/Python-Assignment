''' ID:-20CS063    NAME:Hemil Patoliya'''
'''AIM:- Some words may repeat'''

n = int(input().strip())

dict = {} #for count the specific word
list = []  # for store given word

for i in range(n):
  j = input().strip()
  if j in dict:
    dict[j] += 1 #increment
  else:
    dict[j] = 1
    list.append(j) #store that word
    
print(len(list))
print(' '.join([str(dict[j]) for j in list])) #show how many times word come