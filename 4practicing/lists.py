# how many matches do you have from the list

mylist = [2, 4, 43, 17, 21, 7]
mylist2 = [13, 21, 17, 30, 3, 5]

mylist.sort()
mylist.sort()

result = set(mylist).intersection(set(mylist2))
print(result)
