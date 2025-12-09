#Dictionaries in python - Dictionaries are used to store data values in "key":value pairs.They are unordered,mutuable and dont allow duplicate keys
# we can create list and tuples in dictionary also
info = {
    "name":"Pranav",
    "age":22,
    "Department":"AI&DS",
    "PRN" : "22UAD049",
    "subjects":["c","cpp","python","java"],
    "topics" : ("Variables","Keywords","Functions")
}
info["age"] = 24
info["surname"] = "Patil"
print(info)

#Nested Dictionary-
student={
    "name":"pranav",
    "age":22,
    "Department":"AI&DS",
    "score" : {
        "chem":96,
        "cpp":95,
        "python":96
    }
}
student["score"]["chem"]=98
print(student["score"]["chem"])

#Dictionary Methods
print(student.keys())#->returns all keys from dictionary
print(student.values())#-> returns all values from dictionary
print(student.items())#-> returns all key-value pairs as tuples
print(student.get("key"))#->returns value according to key
student.update({"PRN":"22UAD049","city":"Gadhinglaj"})#-> inserts the specified items to the dictionary
print(student)

# Sets in python 
#set is the collection of the unordered items.Each element in the set must be unique and immutable 
#in set repeated elements stores only once
collection = {1,2,3,4,5,4,3,2,4,4,2}
info={1,2,2,3,4,5,3,2,1,6,7}
#print(collection)
#code to create empty set 
#info=set()
#print(info)

#Methods in set 
collection.add(6)#->adds an element
print(collection)
collection.remove(5)#->it removes the element
print(collection)
collection.pop()#removes a random value
print(collection)
collection.clear()#->empaties the set
print(collection)
print(collection.union(info))#->combines both set values and returns new
print(collection.intersection(info))#->combines common values and returns new 

# Practice Questions 

# store following word meaning in a python dictionary
#table:"a piece of furniture","list of facts and figures"
#cat:"a samll animal"
dictionary ={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(dictionary)

#2.you are given a list of subjects for students.Assume one classroom is required for 1 subject.how manny classrooms are needed by eaech student
#"python","java","c++","python","js","java","python","java","c++","c"
subjects = {"python","java","c++","python","js","java","python","java","c++","c"}
print(subjects)
print(len(subjects))

#3.WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with
#an empty dictionary and add one by one.Use subject name as key & marks as value
marks={}
x=int(input("enter physics: "))
marks.update({"phy":x})
y=int(input("enter chemistry: "))
marks.update({"chem":y})
z=int(input("enter math: "))
marks.update({"math":z})
print(marks)

#Figure out a way to store 9 & 9.0 as seprate values in the set
values={("float",9.0),("int",9)}
print(values)