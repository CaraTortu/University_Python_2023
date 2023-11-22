import json

with open("students.json") as f:
    student_details = json.load(f)["studentDetails"]

computing_students = []

for user in student_details:
    if user.get("course") == "Computing":
        computing_students.append(user)

    print(f"Name: {user.get('name')}\nSubjects: {', '.join(user.get('subjects'))}")
    
with open("computing.json", "w") as f:
    json.dump(computing_students, f)
    
