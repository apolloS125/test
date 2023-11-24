def convert_length():
    user_input = input("Enter value in mm, cm, and m: ")
    units = ["mm", "cm", "m"]

    valid_input = False
    value = None
    current_unit = None

    for unit in units:
        if unit in user_input:
            try:
                value = float(user_input.replace(unit, "").strip())
                current_unit = unit
                valid_input = True
                break
            except ValueError:
                continue

    if not valid_input or value is None or current_unit is None:
        print("Invalid input format. Please try again.")
        return

    print("Enter unit to convert in mm, cm, m:")
    for idx, unit in enumerate(units):
        print(f"{idx + 1}. {unit}")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice not in range(1, 4):
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    target_unit = units[choice - 1]

    # Conversion logic
    if current_unit == "cm":
        if target_unit == "mm":
            result = value * 10
        else:
            result = value / 100
    elif current_unit == "mm":
        if target_unit == "cm":
            result = value / 10
        else:
            result = value / 1000
    else:
        if target_unit == "cm":
            result = value * 100
        else:
            result = value

    print(f"Value after unit conversion is {result}{target_unit}")


convert_length()
