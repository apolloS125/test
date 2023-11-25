value = input("Enter value in mm, cm, and m: ")
unit = input("Enter unit to convert in mm, cm, m: ")

if "cm" in value and unit == "mm":
    result = float(value.replace("cm","")) * 10
    print(f"Value after unit conversion is {result}mm")
elif "cm" in value and unit == "m":
    result = float(value.replace("cm","")) / 100
    print(f"Value after unit conversion is {result}m")
elif "mm" in value and unit == "cm":
    result = float(value.replace("mm","")) / 10
    print(f"Value after unit conversion is {result}cm")
elif "mm" in value and unit == "m":
    result = float(value.replace("mm","")) / 1000
    print(f"Value after unit conversion is {result}m")
elif "m" in value and unit == "cm":
    result = float(value.replace("m","")) * 100
    print(f"Value after unit conversion is {result}cm")
elif "m" in value and unit == "mm":
    result = float(value.replace("m","")) * 1000
    print(f"Value after unit conversion is {result}mm")