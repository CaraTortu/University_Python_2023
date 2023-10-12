grade = input("Grade: ")

values = ["F", "D", "C", "B", "A"]
n_value = values.index(grade[0])

if len(grade) <= 1:
    print(n_value)
    exit(0)

if grade[0] in ["B", "C", "D"]:
    n_value += 0.3 if grade[1] == "+" else -0.3

elif grade == "A-":
    n_value -= 0.3

print(n_value)

