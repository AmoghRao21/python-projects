def celsius_to_fahrenheit(celsius) :
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit) :
    return (fahrenheit - 32) * 5/9

def get_temp_input(prompt) :
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid Temperature")
            

def get_conversion_choice():
    while True:
        choice = input("Enter C for Celsius, F for fahrenheit:").strip().upper()
        if choice in ('C','F'):
            return choice
        else:
            print("Invalid Choice.")
            

def main():
    print("WELCOME TO TEMPERATURE CONVERTER")
    choice = get_conversion_choice()
    
    if choice == 'C':
        celsius = get_temp_input("Enter The Temp in Celsius: ")
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(fahrenheit)
    elif choice == 'F':
        fahrenheit = get_temp_input("Enter Temp In Fahrenheit: ")
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(celsius)
        
if __name__ == "__main__":
    main()