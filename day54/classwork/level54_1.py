def division_calculator():
    try:
        numerator = float(input("Please enter the numerator: "))
        denominator = float(input("Please enter the denominator: "))

        if denominator == 0:
            raise ValueError("Cannot divide by zero!")
        result = numerator / denominator
        print(f"The result is {result}")

    except ValueError as ve:
        print(f"Error: {ve}")

    finally:
        print("Operation complete.")

division_calculator()