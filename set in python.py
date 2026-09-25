collection={1,2,4,"hello","world"}
print(collection)
print(type(collection))

nums={1,2,3,2,3,4}#repeated elements stored only once, so it is resolved
print(nums)
print(len(nums))

null_set=set()#empty set syntax
print(null_set)
print(type(null_set))

#set methods
set1=set()
set1.add(1)#adds an element
set1.add(2)
set1.add(3)
set1.add(2)
set1.add("hello world")
set1.add((1,2,3))
print(set1)

set1.remove(3)#removes an element
print(set1)
print(len(set1))#returns length of the set
print(set1.pop())#removes a random value
print(set1.clear())#removes all elements

set2={1,2,3,4,5}
set3={4,5,6,7,8}
print(set2.union(set3))#returns union of two sets
print(set2.intersection(set3))#returns intersection of two sets
print(set2.difference(set3))#returns a new set with elements in the first set but not in both
print(set2.issubset(set3))#checks if the first set is a subset of the second set
print(set2.issuperset(set3))#checks if the first set is a superset of the second set
