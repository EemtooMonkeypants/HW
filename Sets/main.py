set1 = {1,2,3}
print(set1)
for i in set1:
    print (i)
set1.add("green")
print(set1)
set1.remove(1)
print(set1)
print(6 in set1)

set11 = {1,2,3,4}
set2 = {4,5,6,7}
banana = set11.union(set2)
print(banana)

#intersection
apple = set11.intersection(set2)
print(apple)

#difference
blueberry = set11.difference(set2)
print(blueberry)

#symmetrydifference
strawberry = set11.symmetric_difference(set2)
print(strawberry)