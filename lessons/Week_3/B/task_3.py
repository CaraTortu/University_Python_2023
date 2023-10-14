import random

val_a = random.randint(1, 12)
val_b = random.randint(1, 12)

lives = 3

while lives != 0:
    res = int(input(f"What is {val_a}*{val_b}?: "))

    if res != val_a * val_b:
        lives -= 1
        print(f"Mistake! You have {lives} tries left.")
    else:
        print("Correct!")
        exit(0)

print(f"You ran out of tries! The answer was: {val_b*val_a}")

