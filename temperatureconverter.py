def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print("Temperature Converter")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

choice = input("Enter choice (1 or 2): ")
temp = float(input("Enter temperature: "))

if choice == "1":
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result:.2f}°F")
elif choice == "2":
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {result:.2f}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")