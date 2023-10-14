n = 0

while True:
    price = input("Price [q, Q to quit]: ")
    
    if price.isdigit():
        n += int(price)
        continue
    
    if price.lower() == "q":
        break

    print("ERROR: Invalid character")

print(f"Your total amount is: {n}€")
