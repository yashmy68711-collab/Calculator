print("====== Smart Calculator ======")

history = []

while True:
    print()
    print("Choose operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Show History")
    print("6 - Exit")

    choice = input("Enter choice: ")

    if choice == "6":
        print("Exiting...bye")
        break

    if choice == "5":
        if len(history) == 0:
            print("No history yet")
        else:
            print("--- Calculation History ---")
            for item in history:
                print(item)
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice, try again")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except:
        print("Please enter valid numbers")
        continue

    if choice == "1":
        result = a + b
        history.append(f"{a} + {b} = {result}")

    elif choice == "2":
        result = a - b
        history.append(f"{a} - {b} = {result}")

    elif choice == "3":
        result = a * b
        history.append(f"{a} * {b} = {result}")

    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
            continue
        result = round(a / b, 2)
        history.append(f"{a} / {b} = {result}")

    print("Answer is:", result)