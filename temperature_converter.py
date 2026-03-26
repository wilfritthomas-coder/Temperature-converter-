"""
Temperature Converter Program
Task 4: Cognifyz Technologies
Converts temperatures between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the formula: F = (C × 9/5) + 32"""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using the formula: C = (F − 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9


def get_temperature_input(unit: str) -> float:
    """Prompt the user to enter a valid temperature value."""
    while True:
        try:
            temp = float(input(f"\nEnter the temperature in {unit}: "))
            return temp
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value (e.g. 100, -40, 37.5).")


def get_conversion_choice() -> str:
    """Prompt the user to choose a conversion direction."""
    print("\n" + "=" * 45)
    print("       TEMPERATURE CONVERTER")
    print("=" * 45)
    print("  [1]  Celsius  →  Fahrenheit")
    print("  [2]  Fahrenheit  →  Celsius")
    print("  [3]  Exit")
    print("=" * 45)

    while True:
        choice = input("Select an option (1 / 2 / 3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("  ⚠  Invalid choice. Please enter 1, 2, or 3.")


def display_result(original_value: float, original_unit: str,
                   converted_value: float, converted_unit: str) -> None:
    """Display the conversion result in a formatted way."""
    print("\n" + "-" * 45)
    print("  RESULT")
    print("-" * 45)
    print(f"  {original_value:.2f}° {original_unit}  =  {converted_value:.2f}° {converted_unit}")
    print("-" * 45)


def run_converter() -> None:
    """Main loop that drives the temperature converter."""
    print("\nWelcome to the Temperature Converter!")

    while True:
        choice = get_conversion_choice()

        if choice == "3":
            print("\nThank you for using the Temperature Converter. Goodbye!\n")
            break

        elif choice == "1":
            celsius = get_temperature_input("Celsius (°C)")
            fahrenheit = celsius_to_fahrenheit(celsius)
            display_result(celsius, "Celsius", fahrenheit, "Fahrenheit")

        elif choice == "2":
            fahrenheit = get_temperature_input("Fahrenheit (°F)")
            celsius = fahrenheit_to_celsius(fahrenheit)
            display_result(fahrenheit, "Fahrenheit", celsius, "Celsius")

        again = input("\n  Convert another temperature? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the Temperature Converter. Goodbye!\n")
            break


if __name__ == "__main__":
    run_converter()
