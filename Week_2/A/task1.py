subjects = ["Python", "Mathematics", "Computer systems"]
results = []

name = input("Student name: ") 

for i in subjects:
    answer = input(f"Enter result for {i}: ")
    results.append(float(answer))

"""
m = max([len(i) for i in subjects])

print(name)
for (i, j) in zip(subjects, results):
    print(f"{i}{(m-len(i) + 10) * ' '}{j}")
"""

print(f"{subjects[0]:<20} {results[0]:>2}",
      f"\n{subjects[1]:<20} {results[1]:>2}",
      f"\n{subjects[2]:<20} {results[2]:>2}")

