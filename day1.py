# first program
#print("hello")


# we can use python as calculator also
# print(43+43)
# print(45-43)
# print(43*43)
# print(100/50)


# variabels in python
# Variable - it is a name given to memory location in program 
# variable name should be simple,short and meaningful
#name = "Pranav"
#age = 22
#age2 = age
#print("my name is: ",name)
#print("my age is: ",age2)

# method to  find type of variable - python detects type of variable automatically
#print(type(name))
#print(type(age))

# data types in python 
# 1.Integer - stores numerical whole values
# 2.String - stores textual data
# 3.Float - Stores decimal values
# 4.Boolean - stores true or false
# 5.None - represents where we dont want to store any type of value

#age = 22
#old = False
#a = None
#
#print(type(age))
#print(type(old))
#print(type(a))

# keywords in python - keywords are reserved words in python
# e.g - and,as,assert,break,class,continue,def,del,elif,else,except,finally,false,for,from,global etc


# code to find sum of two numbers 
#a=2
#b=3
#sum=a+b
#print(sum)


# opertaors in python 

# 1. Arithmetic Operators(=,-,*,/,%,**)
#a=3
#b=5
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
#print(a**b)

# 2. Relational/Comparison operators(==,!=,>,<,>=,<=)
#a=50
#b=70
#print(a==b)
#print(a!=b)
#print(a>b)
#print(a<b)
#print(a>=b)
#print(a<=b)

# 3. Assignment Operators(=,+=,-=,*=,/=,%=,**=)
#a=50
#a+=10
#print(a)

# 4. Logical Operators(not,and,or)
#a=50
#b=30
#print(not(a>b))
 # and - gives true if both conditions are true
 # or - gives true if one of the condition is true


# Type Conversion- when we convert one type of variable to another type of variable 
#a=2
#b=4.25
#sum = a+b
#print(sum)


# Type casting - we convert manually in code 
#a=int("2")
#b=4.25
#print(a+b)

# input in python - input()statement is used to accept values(using keyboard) from user
# result for input() is always a str

#a = int(input("Enter the value of a: "))
#b=int(input("Enter the value of b: "))
#print(a+b)

# WAP to input side of square & print its area

#side = int(input("enter the side of the square: "))
#area = side * side
#print("Area of the square is : ",area)

# WAP to input 2 floating point numbers and print their avg
#a=float(input("enter the value of a: "))
#b=float(input("enter the value of b: "))
#avg = (a+b)/2
#print(avg)

# WAP to input 2 int numbers,a and b.print true if a is greater than or equal to b.if not print false
#a=float(input("enter the value of a: "))
#b=float(input("enter the value of b: "))
#print(a>=b)

# Strings - it is a data type that stores a sequence of characters and Strings are immutable
# Basic operations - 
# 1. concatenation - "hello" + "world" -> "helloworld"
# 2. length of str - len(str)
#str1 = "Pranav  "
#str2 = "Patil"
#print(str1+str2)
#print(len(str1))
#print(str1[0]) 

# Slicing - Accessing part of the string
# str[starting_idx:ending_idx] ending index is not included
# str[:4] is same as str[0:4]
#str[1:] is same as str[1:len(str)]
#str = "PranavPatil"
#print(str[2:5]) 

#Slicing with negative index->starts from last
#str="Apple"
#print(str[-3:-1])

# String Functions:
#str = "i am a Engineer."
#print(str.endswith("er.")) #-> return true if string ends with given sub string 
#print(str.capitalize())#->capitalize 1st cahracter
#print(str.replace("e","f"))#->replace all occurance of old with new 
#print(str.find("Eng"))#->return 1st index of 1st occurance
#print(str.count("eer"))#->count the occurance of substr in string

# Practice Questions 
# WAP to input users first name and print its length

#first_name = input("enter your first name: ")
#print(len(first_name))

# WAP to find the occurrence of $ in a String
#str = input("Enter the string: ")
#print(str.count("$"))


# Conditional Statements
#age = int(input("enter your age: "))
#if(age>=18):
#    print("can vote")
#else:
#    print("cant vote")

# code to assign grades to student according to their marks

#marks = int(input("enter marks of the students: "))
#if(marks>=90):
#    print("Grade A")
#elif(90>marks>=80):
#    print("Grade B")
#elif(80>marks>=70):
#    print("Grade C")
#else:
#    print("Grade D")

# nested conditional Statement
#age = 8
#if(age>=18):
#    if(age>=80):
#        print("cant drive")
#    else:
#        print("can drive")
#else:
#    print("cant drive")

# Pratice questions
#WAP to check if a number entered by the user is odd or even 
#number = int(input("enter the nnumber: "))
#if(number%2==0):
#    print("number is even")
#else:
#    print("number is odd")

# WAP to find the greatest of 3numbers entered by the user
#a=int(input("enter 1st number"))
#b=int(input("enter 2nd number"))
#c=int(input("enter 3rd number"))
#if(a>b and a>c):
#    print("a is greater")
#elif(b>=c):
#    print("b is greater")
#else:
#    print("c is greater")

# WAP to check the number is multiple of 7 or not 
#number = int(input("enter the number: "))
#if(number % 7 == 0):
#    print("multiple of 7")
#else:
#    print("not a multiple of 7")


# List - A built-in data type that stores set of values.it can store elements of different types wrriten inside the square bracket seprated by comma.
# list are mutuable in python 
#marks = [30,50,70,80,40]
#marks[0] = 100
#print(marks[0])

# slicing is also possible into the list and negative slicing also
#print(marks[1:4])

# methods in list 
#list = [1,2,3]
#list.append(4)#->adds one element at the end
#print(list)
#list.sort()#->sort in ascending order
#print(list)
#list.sort(reverse=True)#->Sort in descending order
#print(list)
#list.reverse()#->reverse the list
#print(list)
#list.insert(4,5)#->insert element at index
#print(list)
#list.remove(2)#->removes first occurence of element
#print(list)
#list.pop(3)#->removes elelment at index
#print(list)

#Tuples in python - A built-in data type that lets us create immutable sequence of values 
# written in paranthesis seprated by comma 
# we can create tuple with no values also and we can create tuple with only one value also 
# tup = (1,)->we use comma to treat it as a tuple
#tup = (1,2,3,4,5,6)
# we can do slicing in tuple also 
#print(tup[1:4])

#tuple methods
#print(tup.index(2))#->returns index of first occurrence 
#print(tup.count(3))#->count total occurrances


#practice questions 
# WAP to ask the user to enter names of their 3 fav movies and store them in list 
#movies = []
#movies.append(input("enter 1st movie: "))
#movies.append(input("enter 2nd movie: "))
#movies.append(input("enter 3rd movie: "))
#print(movies)

# WAP to check if a list contains a palindrome of elements

#list = ["m","a","m"]
#list1 = list.copy()
#list1.reverse()
#if(list == list1):
#    print("palindrome")
#else:
#    print("not")

# WAP to count the number of students with the "A" grade in the following tuple

#grade=("C","D","A","A","B","B","A")
#print(grade.count("A"))