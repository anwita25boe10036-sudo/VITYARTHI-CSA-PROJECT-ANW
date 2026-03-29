# VITYARTHI-CSE-PROJECT-ANW
## STUDENT GRADE CALCULATOR - Project Documentation

## Project Overview :-
Many teachers, professors, and educational institutions need a simple way to organize and calculate student grades efficiently. Without adequate grade management tools, it is difficult to track student performance, calculate overall scores, and determine final grades accurately. This can lead to calculation errors, inefficiencies in grading, and potential unfairness in student assessment. Addressing this problem is crucial, practical, and relevant in education. Finding a solution will enhance grading accuracy, improve educational operations, and reduce mistakes. There is a need for an easy-to-use tool that helps educators manage student grades effectively.

### Problem definition:
In many educational institutions, especially smaller schools or those with limited resources, student grades, including names, subjects, and scores, are often recorded manually or in unstructured formats. This makes it difficult to calculate accurate averages, increases the likelihood of calculation errors, and leads to inefficient grade management and delays in reporting. This system aims to solve this issue by providing a basic yet effective digital solution for grade calculation and management.


## Objectives :-

Objectives:

•To create a Python-based system that collects and manages students’ grades.

•Centralize student grade information in one digital location.

•Provide a straightforward way to add new students and their grades and review or update existing records as needed.

•Reduce manual calculation time and effort, thus improving efficiency.

•Introduce digital grade management to users worldwide.


## Installation and Setup:-

Step 1: Install Python
Download and install Python from: https://www.python.org/downloads/

Step 2: Download the Project
Clone the repository from GitHub:(https://github.com/anwita25boe10036-sudo/VITYARTHI-CSA-PROJECT-ANW)

Go to project folder:cd ANWITA DWIVEDI

Step 3: Run the Program
python ANWITA DWIVEDI.py The program will start and show the menu
   

## How to use :-

Step 1: Start.

Step 2: Print "Program: Student Grade Calculator."

Step 3: Create an empty list for student records, named students.

Step 4: Define the 'addStudent' function with parameters name, subject, and grade.

a. Accept the name, subject, and grade in a dictionary named student.

b. Insert this dictionary into the 'students' list using the append function.

c. Print f"Student {name} added."

Step 5: Define a function, 'viewStudents', with no parameters, to display all student records.

a. Check if the length of the list 'students' is zero, then print "No records found."

b. Otherwise, loop through to print all student details as stored.

Step 6: Define a function, 'updateGrade', with 'studentname' and 'newgrade' as parameters.

a. Use a loop to iterate through 'students'.

b. Check if the student's name equals 'studentname', and if so, update the grade; print the new grade and the student's name.

c. Otherwise, print f"Could not find student named {studentname}."

Step 7: Define a function, 'calculateAverage', with no parameters.

a. If no students exist, print "No students to calculate."

b. Otherwise, calculate the average grade of all students and display it.

Step 8: While this loop is true,

a. Print "\n Student Grade Management System."

b. Print "1) Add a new student's record."

c. Print "2) Show all student records."

d. Print "3) Update a student's grade."

e. Print "4) Calculate average grades."

f. Print "5) Exit program."

• Take input from the user to select an option from 1 to 5.

• If option equals 1, accept the student's name, subject, and grade; call the 'addStudent' function.

• If option equals 2, call the 'viewStudents' function.

• If option equals 3, accept the student's name and new grade; call 'updateGrade'.

• If option equals 4, call 'calculateAverage' function.

• If option equals 5, print "Program closed."; use the break function to exit.

• Otherwise, print "Invalid option! Choose a number from 1 to 5."

Step 9: End.


