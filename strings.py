str1="This is a string. We creating it in a python"
print(str1)

str2="This is a string. \n We creating it in a python"#\n is the newline character ,used to break a line of text and start a new one
print(str2)

str3="This is a string. \tWe are creating it in a python"#\t is an escape sequence, python interpreter replaces it with a whitespace gap.
print(str3)

str4="hello"
str5="world"
print(len(str5))
final_str=str4+" "+str5#concatenating two strings 
print(final_str)
print(len(final_str)) #calculating the length of the string

str="hello world"
ch=str[2] #indexing
print(ch)
print(str[5])

#slicing
print(str[0:4])
print(str[:4])#[0:4]
print(str[3:])#[3:len(str)]
print(str[3:len(str)])
print(str[-3:-1])

#string functions
print(str.endswith("ld"))
print(str.endswith("hell"))

print(str.capitalize())#capitalizes the 1st char

print(str.replace("o","a"))#replaces all the occurrences of old with new

print(str.find("l"))#returns 1st index of 1st occurer
print(str.find("a"))#returns -1

print(str.count("l"))#counts the occurrences of substr


