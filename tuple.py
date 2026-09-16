tup=(34,45,56,67,78)
print(tup)
print(tup[2])

tup1=(1)
print(tup1)
print(type(tup1))

tup2=("hello",)
print(tup2)

#tuple methods
tup3=(1,2,3,4,5,6)
print(tup3.index(2))#returns index of the first occurrence
print(tup3.count(1))#counts total occurrences
print(max(tup3))#returns the largest value in the tuple
print(min(tup3))#returns the smallest value in the tuple

tup4=(4,3,6,5,8)
print(sorted(tup4))#returns a new sorted list from the elements of the tuple

tup5=(1,2)
tup6=(3,4,5)
print(tup5+tup6)#combines two tuples