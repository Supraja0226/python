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


s=" Hello "
print(s.lower())#conerts all the characters in a string into lowercase
print(s.upper())#converts all the characters in a string into uppercase
print(s.strip())#removes the leading and trailing whitespaces from the string
print(s.split())#splits the string into a list of substrings based on whitespace
print(''.join(["hello","world"]))#joins the list of strings into a single string
print(s.replace("Hello","Hi"))#replaces the specified substring with the new substring in the string
print(s.count("l"))#returns the number of times a specified value appears in the string
print(s.find("o"))#returns the index of the first occurrence of a specified value in the string
print(s.startswith("H"))#returns True if the string starts with the specified value
print(s.isalpha())#returns True if all characters in the string are alphabets
print(s.isdigit())#returns True if all the characters in the string are digits

x=-10;
print(abs(x))#returns the absolute value of a number

a=4;
b=2;
print(pow(a,b))#returns the value of a raised to the power of b

y=3.14;
print(round(y))#returns the value of a number rounded to the nearest integer

print(max(1,2,3,4))#returns the largest value among the specified values