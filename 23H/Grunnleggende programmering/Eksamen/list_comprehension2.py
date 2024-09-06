list1 = [1,2,3,4,5,10,11,12,13,14,15,16]

# create a list containing the elements of list1 that are even numbers above 10.
list2 = [i for i in list1 if i > 10 and i % 2 == 0]
print(list2)