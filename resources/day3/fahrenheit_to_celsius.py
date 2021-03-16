"""
Given a temperature in Fahrenheit, return it in Celsius
"""

print()

# Ask a temperature in Fahrenheit
temp_in_fa = int(input("What's the temp in Fahrenheit?: "))

# Calculate it in Celsius
celsius = (temp_in_fa - 32) * 5/9

# Tell the user what it is
print(f"\nTemp in Celsius is: {str(round(celsius, 0))}")

print()
