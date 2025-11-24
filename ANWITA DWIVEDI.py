print("PROGRAM: Student Grade Calculator")
def inputmarks(num_subjects):
   
    marks = []
    for i in range(num_subjects):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input, please enter a numeric value.")
    return marks

def calculate_average(marks):
   
    total = sum(marks)
    average = total / len(marks)
    return average

def determine_grade(average):
    
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def print_student_report(student_name, marks, average, grade):
   
    print(f"Report for {student_name}:")
    print("Marks:", marks)
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

def main():
    print("Student Grade Calculator")
    student_name = input("Enter the student's name: ")
    num_subjects = 5  
    marks = inputmarks(num_subjects)
    average = calculate_average(marks)
    grade = determine_grade(average)
    print_student_report(student_name, marks, average, grade)
    pass

if __name__ == "__main__":
    main()