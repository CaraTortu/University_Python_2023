amount_of_student = int(input("Student Amount: "))

grades = []

for i in range(amount_of_student):
    grade = int(input(f"Grade for student {i+1} [0-100]: "))
    
    while grade < 0 or grade > 100:
        print("ERROR: must be between 0-100.")
        grade = int(input(f"Grade for student {i+1} [0-100]: "))
    
    grades.append(grade)

print(f"Max grade: {max(grades)}")
print(f"Minimum grade: {min(grades)}")
print(f"Passing students: {len([i for i in grades if i > 40])}")
print(f"Failing students: {len([i for i in grades if i <= 40])}")
print(f"Average: {sum(grades) / len(grades)}")
