days_in_months = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 30,
    "Apr": 31,
    "May": 30,
    "Jun": 31,
    "Jul": 30,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

# Print the months and the amount of days_in_months that they have
for key, value in days_in_months.items():
    print(f"{key} has {value} days")

# Prompt the user to enter a month and display the amount of days_in_months
month = None
while month not in days_in_months:
    month = input(
        f"Please enter a month to see days from. [{', '.join(i for i in days_in_months)}]: ")

print(f"{month} has {days_in_months[month]} days")

# Prompt the user to enter a no of days_in_months and print the months with the number of days_in_months
amount_of_days = int(input("Amount of days: "))

months = list(
    filter(lambda item: item[1] == amount_of_days, days_in_months.items()))
months = list(map(lambda x: x[0], months))

print(f"{', '.join(months)} have {amount_of_days} days")

# Prompt the user to input a letter and print the months that start with such letter
letter = input("Letter: ").lower()

months = list(
    filter(lambda item: item[0].lower() == letter, days_in_months.keys()))

print(f"{', '.join(months)} start with the letter {letter}")
