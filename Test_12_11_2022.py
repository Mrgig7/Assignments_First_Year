# Solve these Questions using loops and recursion

# 1.	Find Sum of numbers from 1 to n 
# find out the sum of numbers from 1 to n like 1 + 2 + 3 + 4 +, etc

# A Simple Python program to compute sum
# of digits in numbers from 1 to n

# Returns sum of all digits in numbers
# from 1 to n
# Sum of natural numbers up to num

num = int(input())

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print(sum)

# or 

# A Simple Python program to compute sum
# of digits in numbers from 1 to n

# Returns sum of all digits in numbers
# from 1 to n
def sumOfDigitsFrom1ToN(n) :

	result = 0 # initialize result

	# One by one compute sum of digits
	# in every number from 1 to n
	for x in range(1, n+1) :
		result = result + sumOfDigits(x)

	return result

# A utility function to compute sum of
# digits in a given number x
def sumOfDigits(x) :
	sum = 0
	while (x != 0) :
		sum = sum + x % 10
		x = x // 10
	
	return sum


# Driver Program
n = int(input())
print("Sum of digits in numbers from 1 to", n, "is", sumOfDigitsFrom1ToN(n))

# Reverse a string 

x = input()
txt = x[::-1]

print(txt)

# Adding all numbers in a list 

# Python program to find sum of all
# elements in list using recursion

# creating a list
list1 = [11, 5, 17, 18, 23]

# creating sum_list function


def sumOfList(list, size):
	if (size == 0):
		return 0
	else:
		return list[size - 1] + sumOfList(list, size - 1)


# Driver code
total = sumOfList(list1, len(list1))

print(total)

#or

# Python program to find sum of elements in list

total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)

#1.# we need to write a python program to find the power of a number using recursion
# input : num = 2, power= 3
# output : 8

# Python3 code to recursively find
# the power of a number

# Recursive function to find N^P.
def power(N, P):

	# If power is 0 then return 1
	# if condition is true
	# only then it will enter it,
	# otherwise not
	if P == 0:
		return 1

	# Recurrence relation
	return (N*power(N, P-1))


# Driver code
if __name__ == '__main__':
	N = 5
	P = 2

	print(power(N, P))

# Assign a different name to function and call it through the new name

def my_age(name, age):
    print(name, age)

# call using original name
my_age("Emma", 26)

# assign new name
showStudent = my_age
# call using new name
showStudent("Emma", 26)

# Python Program to Print All Odd Numbers in a Range

# Python program to print Even Numbers in given range

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

# iterating each number in list
for num in range(start, end + 1):

	# checking condition
	if num % 2 != 0:
		print(num)

#or

# Uncomment the below two lines for taking the User Inputs
#start = int(input("Enter the start of range: "))
#end = int(input("Enter the end of range: "))

# Range declaration
start = 5
end = 20

if start % 2 != 0:

	for num in range(start, end + 1, 2):
		print(num, end=" ")
else:

	for num in range(start+1, end + 1, 2):
		print(num, end=" ")

# Python Program to Check Whether a Given Number is Even or Odd using Recursion

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!")

# Python Program to Check whether a Number is Prime or Not using Recursion

def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 'True'
n=int(input("Enter number: "))
check(n)

# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

n = int(input("Number: "))
for i in range(0,n):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)
    

# Python Program to Check if a Number is a Palindrome

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

# Python Program to Count the Number of Vowels in a String

string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

# Python Program to Remove Odd Indexed Characters in a string

def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=input("Enter string: ")
print("Modified string is: ")
print(modify(string))

# Python Program to Remove the nth Index Character from a Non-Empty String

def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))

# Python Program to Replace Every Blank Space with Hyphen in a String

string=input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)

# Python Program to Calculate the Length of a String Without using Library Functions

string=input("Enter string:")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

#  Python Program to Count Number of Lowercase Characters in a String

string=input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

# Python Program to Count the Number of Vowels in a String

string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

# Python Program to Count Number of Uppercase and Lowercase Letters in a String

string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)

# Python Program to Find Common Characters in Two Strings

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

# String Palindrome Program in Python

statement =input(("Enter a letter:"))  
if(statement==statement[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")  

# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=input("Enter string:")
ch=input("Enter character to check:")
print("Count is:")
print(check(string,ch))