# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

grade = int(input("Grade: "))
if (grade<60): print("F")
elif (grade>=60 and grade<=69): print("D")
elif (grade>=70 and grade<=79): print("C")
elif (grade>=80 and grade<=89): print("B")
else: print("A")