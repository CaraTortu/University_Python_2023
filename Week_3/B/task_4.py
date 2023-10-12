import random

calculation = int(input("How many calculation in this test? "))
good = 0

for i in range(calculation):
    a = random.randint(1, 12)
    b = random.randint(1, 12)

    try_result = int(input(f"\tQuestion {i+1}: {a}*{b} = "))

    if try_result != a*b:
        print(f"\t\tINCORRECT {a}*{b} = {a*b}")
    else:
        print(f"\t\tWell done!")
        good += 1

print(f"You scored: {good}/{calculation}")

