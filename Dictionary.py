dict={"name":"Supraja","age":21,"city":"Hyderabad","marks":945}
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["city"])
print(dict["marks"])
dict["age"]=22
print(dict)
print(type(dict))

info={
    "subjects":["Python","Java"],
    "topics":("dict","set","list")
}
print(info)
print(type(info))
print(info["subjects"])
print(info["topics"])

null_dict={}
null_dict["name"]="Sujana"
print(null_dict)

#nested dictionary
student={
    "name":"Supraja",
    "subjects":{
        "phy":94,
        "chem":96,
        "maths":95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

#Dictionary methods
print(student.keys())#returns all keys
print(student.values())#returns all values
print(student.items())#returns all (key, val)pairs as tuples
print(student.get("name"))#returns the key according to value
student.update({"age":17})#inserts the specified items to the dictionary
print(student)
print(student.pop("age"))#removes the speified key and returns its value 
print(student.popitem())#removes and returns an arbitary pair from the dictionary
new_dict=student.copy()#returns a shallow copy of the dictionary
print(new_dict)
print(len(student))#returns the number of items in ith dictionary
student.clear()#removes all items from the dictionary
print(student)
