def temp_conversion():
    celsius_temp = int(input("Enter the temperature in celsius: "))
    fahrenheit_temp = 9/5 * (celsius_temp) + 32
    print(f"The temperature in fahrenheit is {fahrenheit_temp:.1f}")

temp_conversion()