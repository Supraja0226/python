marks=[45.5,59.0,38.5,42.5,43.0]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

student=["Ramya",46.5,19,"Hyderabad"]
print(student)
student[0]="Sujana"
print(student)

marks1=[20,30,40,50,60,70,80]
print(marks1[:6])
print(marks1[0:])
print(marks1[::-1])
print(marks1[-5:-1])

#list methods
lst=[1,2,3,4]
lst.append(5)#adds one element at the end
print(lst)

lst1=[3,6,2,1,5,9,8,7]
lst1.sort()#sorts in ascending order
print(lst1)
lst1.sort(reverse=True)#sorts in descending order 
print(lst1)
lst1.reverse()#reverse the list
print(lst1)

lst2=[2,1,3]
lst2.insert(1,4)#insert element at index
print(lst2)
lst2.remove(2)#removes first occurrence of element
print(lst2)
lst2.pop(2)#removes element at index
print(lst2)

lst3=[1,2,3,4,5]
lst3.extend([6,7])#add all elements of a list to another list
print(lst3)
lst3.clear()#removes all the elements from the list
print(lst3)

lst4=[4,5,5,6,7,8]
print(lst4.count(5))#returns number of elements with the specified value
lst5=lst4.copy()#returns a shallow copy of the list
print(lst5)
print(lst5.index(4))#returns the index of the first element with the specified value

lst6=[1,2,3,4,5]
print(lst6)
print(lst6[1])
lst6.append(10)
print(lst6)

lst7=[10,20,30,40,50]
lst7.pop(4)
print(lst7)

lst8=[5,2,8,1,3]
lst8.sort()
print(lst8)

