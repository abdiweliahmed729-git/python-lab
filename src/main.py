import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils import square, is_even, celsius_to_fahrenheit


try: 
    user_input = float(input("Enter a number to square: "))

    print(f"The square of {user_input} is {square(user_input)}")
    print(f"Is the number even? {is_even(user_input)}")
    print(f"Celsius to Fahrenheit conversion: {celsius_to_fahrenheit(user_input)}°F")
except ValueError:
    print("Please enter a valid numeric number.")