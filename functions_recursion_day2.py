#function in python- block of statements that perform a specific task
#syntax - 
#def func_name(param1,param2...):
    #somw work
    #return value

# function call -
# func_name(arg1,arg2...)

#def calc_avg(a,b,c):
#    sum = a+b+c
#    avg = sum/3
#    print(avg)
#    return avg
#
#calc_avg(1,2,3)

#types of function-
#1.built in function-print(),len(),type(),range()
#2.user defined functions-the function which are written by programmer

# practice question
#waf to print the length of the list

def print_length(list):
    print(len(list))

values=[1,2,3,4,5,6]
print_length(values)

#waf to print the elements of a list in a single line
def single_line(list):
    for i in list:
        print(i,end=" ")

single_line(values)

# waf to calculate factorial of number n
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)

factorial(5)

#waf to convert usd into rupees
def usd_inr(n):
    inr = n*90
    print(inr)

usd_inr(4)

#recursion - when a function calls itself repeatedly 
# factorial of number using recursion 
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
n=int(input("enter the value of n: "))
print(fact(n))

# write a recursive function to calculate the sum of first n natural numbers 
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
print(sum(5))

#  write a recursive function to print all elements in a list
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

list=[1,2,3,4,5,6,7]
print_list(list,0)