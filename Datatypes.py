#1.Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# ●	Add a new student and their grade.
# ●	Update the grade of an existing student.
# ●	Remove a student from the list.
# ●	Calculate and display the average grade of the class.
# ●	Display the highest and lowest grades in the class.
# Tasks:
# ●	Use lists to store the student names and their corresponding grades.
# ●	Implement functions to add, update, remove, and calculate the average and extreme grades.

student=[]
grade=[]

def add_student():
    name=input("Enter a string:")
    grade=float("Enter a marks:")
    student.append(name)
    student.append(grade)
    print("student added successfully:")
    



