def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

def farheneit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

choice=input()

if choice.upper()=="C":
    celsius=float(input("enter any temperature:"))
    fahrenheit=celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice.upper()=="F":
    fahrenheit=float(input("Enter any temperature:"))
    celsius=farheneit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid choice.Please enter C or F.")
