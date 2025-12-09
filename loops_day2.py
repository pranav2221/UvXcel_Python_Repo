# loops are used to repeat instructions 
#while loops
#syntax - 
#while condition:
    #some work

#practice questions
# 1.print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#2.print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#3.print multiplicatin table of number n
n = int(input("enter the number: "))
i=1
while i<=10:
    print(n*i)
    i+=1

#print the element of the following list using a loop
list=[1,4,9,16,25,36,49,81,100]
i=0
while i<=len(list)-1:
    print(list[i])
    i+=1

#search for a number x in this tuple using loop\
nums=(1,4,9,16,25,36,49,64,81,100)
x=25
i=0
while i<len(nums):
    if(nums[i] == x):
        print("Found at index: ",i)
        break
    else:
        print("finding...")
    i += 1    

# break and continue keyword 
# break - used to terminate the loop when encountered.
#  continue - termminates execution in the current iteration and continues execution of the loop with the next iteration
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

# code to print odd or even number 
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1


# for loops 
# this loops are genrally used for sequential traversal.for traversing list,string,tuples etc
#syntax: 
# for i in list:
    #some work 
# for loop with else 
#for i in list:
    #some work
#else:
    #work when loop ends
#str="pranavpatil"
#for val in str:
#    print(val)

#practice question
#print the elements of the following list using loop
list=[1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(val)

#search for the number x in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
x = 25
idx = 0
for i in tuple:
    if(x==i):
        print("found at:",idx)
    idx+=1
   
# range()-range function returns a sequence of numbers,starting from 0 by default and iincrements by 1(by default)
# and stops before a spsecified number
#range(start?,stop,step?)

# practice question using for and ranage
# print numbers from 1 to 100
for i in range(1,101):
    print(i)

#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# print the multiplication table of number n
n = int(input("enter the number: "))
i=0
for i in range(1,11,1):
    print(n*i)

# pass statement-pass is a null statement that does nothing.
#it  is used as a placeholder for future code 

# wap to find the sum of first n numbers(using while)
n=int(input("enter the value of n:"))
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)

# wap to find the factorial of first n numbers 
n=int(input("enter the value of n:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)