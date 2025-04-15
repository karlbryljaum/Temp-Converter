def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5/9

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    if from_unit == 'C':
        temp_c = value
    elif from_unit == 'F':
        temp_c = f_to_c(value)
    elif from_unit == 'K':
        temp_c = k_to_c(value)
    else:
        raise ValueError("Invalid source unit (use C, F, or K)")

    if to_unit == 'C':
        return temp_c
    elif to_unit == 'F':
        return c_to_f(temp_c)
    elif to_unit == 'K':
        return c_to_k(temp_c)
    else:
        raise ValueError("Invalid target unit (use C, F, or K)")

def show_menu():
    print("\nTemperature Converter")
    print("---------------------")
    print("Use: C for Celsius, F for Fahrenheit, K for Kelvin")
    print("Example input: 100 C to F")

def main():
    show_menu()
    try:
        while True:
            user_input = input("\nEnter conversion (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            parts = user_input.strip().split()
            if len(parts) != 4 or parts[2].lower() != "to":
                print("Invalid format. Use: <value> <from_unit> to <to_unit>")
                continue

            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[3]

            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit.upper()} = {result:.2f} {to_unit.upper()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
