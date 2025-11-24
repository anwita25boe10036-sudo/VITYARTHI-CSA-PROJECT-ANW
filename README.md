# VITYARTHI-CSE-PROJECT-ANW
STUDENT GRADE CALCULATOR - Project Documentation

1. Real World Problem –Basic Student Grade Management :-
Mismanagement of student grades is a significant issue in educationalsettings. Many teachers, professors, and educational institutions need a simple way to organize and calculate student grades efficiently. Without adequate grade management tools, it is difficult to track student performance, calculate overall scores, and determine final grades accurately. This can lead to calculation errors, inefficiencies in grading, and potential unfairness in student assessment. Addressing this problem is crucial, practical, and relevant in education. Finding a solution will enhance grading accuracy, improve educational operations, and reduce mistakes. There is a need for an easy-to-use tool that helps educators manage student grades effectively.
2. Objectives and Expected Outcomes:-
Objectives:
•To create a Python-based system that collects and manages students’ grades.
•Centralize student grade information in one digital location.
•Provide a straightforward way to add new students and their grades and review or update existing records as needed.
•Reduce manual calculation time and effort, thus improving efficiency.
•Introduce digital grade management to users worldwide.
Expected outcomes:
•A functional Python program that:
o Takes student records (such as name, subject, and grades) as input.
o Uses lists, functions, and loops for data processing and grade calculations.
o Adds, updates, and allows viewing of student grade records.
o Calculates average grades and overall performance.This supports better record management.
•A consistent and reliable source for storing information for future academic decisions.
•Increased productivity in grade management.

3. Applied Concepts Learned in Class to Design the Solution:-
• Lists and dictionaries store student grade records.
• Functions perform modular and reusable calculations for averages and totals.
• Loops help the user choose options (to add, view, update grades, or calculate averages).
• User input handling supports dynamic data collection.
• Problem-solving and structured programming techniques are applied.
4. Usage of Appropriate Tools and Programming Techniques:-
The project uses only the Python Standard Library. Key techniques include:
• Modular programming (functions).
• Iterative input collection (loops).
• List-based data storage.
• Conditional logic to choose user options (to add, view, update grades, or calculate averages).
• Console-based user interactions.
• Mathematical operations for grade calculations.
5. Follow a Structured Development Process:-
A. Problem definition:
In many educational institutions, especially smaller schools or those with limited resources, student grades, including names, subjects, and scores, are often recorded manually or in unstructured formats. This makes it difficult to calculate accurate averages, increases the likelihood of calculation errors, and leads to inefficient grade management and delays in reporting. This system aims to solve this issue by providing a basic yet effective digital solution for grade calculation and management.
B. Requirement Analysis:
• The system must accept student information, including name, subject, and grades.
• It must allow users to view any student's grade record.
• It must let users update a student's grades.
• It must calculate and display average grades and overall performance.
• It must present results in a structured format.
• It should be simple and user-friendly.
• It must work on any system with Python installed.
• The code must be readable, modular, and maintainable.
C. Top-Down Design and Modularization:
Main modules:
1.	Input module: Collects a number (1 to 5) from the user, indicating if they want to 1. add a new student record, 2. view all student records, 3. update a student's grades, 4. calculate average grades, or 5. exit.
2.	Processing module:
• 'addStudent(name, subject, grade)' function accepts the student's name, subject, and grade, storing it in a list.
• 'viewStudents()' function shows all student grade records.
• 'updateGrade(studentname, newgrade)' function updates the student's grade.
• 'calculateAverage()' function calculates and displays the average grade of all students.
3.	Output module: Displays the desired output including grade calculations.
Top-Down Approach:
• Begin with the main issue: "Student Grade Management."
• Break the problem into smaller tasks: Input → Processing → Calculation → Output.
• Implement each component step-by-step effectively.
D. Algorithm Development:
Algorithm: Student Grade Calculator
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
E. Implementation:
• Uses lists for data storage.
• Uses loops for input and processing.
• Uses functions for adding, viewing, updating student records, and calculating averages.
• Uses conditional statements.
• Uses mathematical operations for grade calculations.
Test Case	Input	Expected Outcome
1.	Add student record:
Name = "John", Subject = "Math", Grade = 85	The student record is added to the list.
2.	View all student records:
Several students added valid information.	Student details are displayed in a clear, numbered list format.
3.	Update Existing Student Grade:
Existing student name and new grade value.	The student's grade has been updated, and a success message is shown.
4.	Calculate Average Grades:
Multiple students with grades have been added to the system.	Average grade calculated and displayed accurately.
5.	Prevent Invalid Grade Entries:
Attempt to add grade outside valid range (e.g., 105).	Invalid grade rejected with appropriate error message.

	Refinement Activities:-

• Improved category descriptions for educational context.
• Added threshold-based analysis for grade categorization.
• Enhanced textual output formatting for grade reports.
• Ensured code readability and modularity.
• Added input validation for grade values.


