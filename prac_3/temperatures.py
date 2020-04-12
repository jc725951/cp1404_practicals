def main():
    """ To convert temperatures"""

    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if (choice == "C"):
            celsius = float(input("Enter celsius temperature"))
            print("The fahrenheit temperature =", (celsius_to_fahrenheit(celsius)))

        elif (choice == "F"):
            fahrenheit = float(input("enter fahernheit temperature "))
            print("The celsius temperature =", (fahrenheit_to_celsius(fahrenheit)))

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
        """Convert celsius to fahrenheit"""
        return(celsius * 9/50) + 32


def fahrenheit_to_celsius(fahrenheit):
        """ Convert fahrenheit to celsius"""
        return(fahrenheit - 32) * 5/9



main()