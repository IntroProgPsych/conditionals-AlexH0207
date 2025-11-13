# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your code here:

name1 = input("Please type a name for person 1: ")
age1 = int(input("Please type an age for person 1: "))
name2 = input("Please type a name for person 2: ")
age2 = int(input("Please type an age for person 2: "))
if age1>age2: print(f"The elder is {name1}.")
elif age2>age1: print(f"The elder is {name2}.")
else: print(f"{name1} and {name2} are the same age")