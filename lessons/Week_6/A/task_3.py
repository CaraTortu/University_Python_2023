grades = {}


def add_student() -> None:
    student_name = input("What is the student name?: ")
    student_grade = input(f"What is {student_name}'s grade?: '")

    grades[student_name] = student_grade


def remove_student() -> None:
    student_name = input("What is the student name?: ")
    del grades[student_name]


def get_all_grades() -> str:
    results = ""

    for student, result in sorted(grades.items()):
        results += f"{student}: {result}\n"

    return results


def get_option() -> int:
    print(f"What would you like to do?\n1. Add a student\n2. Delete a student/grade\n3. Modify a grade\n4. Print all grades\n0. Quit\n")

    chosen = -1
    while chosen < 0 or chosen > 4:
        chosen = int(input("> "))

    return chosen


if __name__ == "__main__":
    chosen = None
    while chosen != 0:
        chosen = get_option()

        match chosen:
            case 0:
                exit(0)
            case 1:
                add_student()
            case 2:
                remove_student()
            case 3:
                add_student()
            case 4:
                print(get_all_grades())
