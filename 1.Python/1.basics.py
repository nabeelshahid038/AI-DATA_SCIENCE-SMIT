# Rule: Name must start with alphabets.
user_name = "Nabeel" 

# Rule: Names cannot contain spaces.
# Incorrect: student name = "Nabeel" (This will throw an error)

# Rule: You can use underscore (_) symbols[cite: 2].
student_id = 4  # Example of integer variable

# Rule: Reserved words (like 'if', 'else', 'class') cannot be used as names.
# Incorrect: class = "SE" 


# ==========================================
# 2. VARIABLES & DATA TYPES
# ==========================================

x = 4                # Integer
y = 5.5              # Float
message = "Hello!!"  # String

print(f"Message: {message}")
print(f"Values: x={x}, y={y}")


# ==========================================
# 3. OPERATORS & OPERANDS
# ==========================================

# Operators are symbols that perform operations on values (Operands).

# A. Arithmetic Operators:
# Used for mathematical calculations.
a, b = 10, 3
print(f"Addition (+): {a + b}")
print(f"Subtraction (-): {a - b}")
print(f"Multiplication (*): {a * b}")
print(f"Division (/): {a / b}")
print(f"Modulus (%): {a % b}") # Returns the remainder 

# B. Assignment Operators:
# Used to assign values to variables.
z = 50  # Simple assignment (=) 

# C. Comparison Operators[cite: 3]:
# These always return a BOOLEAN value (True or False).
print(f"Is x < y? {x < y}")   # Less Than [cite: 3]
print(f"Is x == y? {x == y}") # Equals [cite: 3]
print(f"Is x != y? {x != y}") # Not Equals [cite: 3]


# ==========================================
# 4. DATA CONVERSION (Intro)
# ==========================================

# Implicit Conversion: Automatic, no data loss (e.g., int to float).
# Explicit Conversion: Manual/Forced, might have data loss (e.g., float to int).

# Example of Explicit:
float_val = 9.9
int_val = int(float_val) # Becomes 9 (Data loss occurs)

# Task1: convert 120F to C and Kelvin (hint: (32°F − 32) × 5/9 = 0°C,	
# 0°C + 273.15 = 273.15K)

fahrenheit = 120
celcius = (fahrenheit - 32) * 5/9
kelvin = celcius + 273.15

print(f"Temperature in Celsius: {celcius:.2f}°C")
print(f"Temperature in Kelvin: {kelvin:.2f}K")

# Task2: convert 493mm into cm, km, mile (hint: 1cm = 10mm, 1km = 100000cm and
# 1mile = 1.60934km)

mm = 493
cm = mm/10
km = cm/100000
mile = km/1.60934

print(f"493mm into cm is : {cm}cm")
print(f"493mm into km is : {km}km")
print(f"493mm into mile is : {mile}mile")

# Task3: convert 38945g into mg, kg and ounce (hint: 1ounce = 28.3495g,
# 1mg = 1000g)

g = 38945
mg = g*1000
kg = g/1000
ounce = g/28.3495

print(f"38945g into mg is : {mg}mg")
print(f"38945g into kg is : {kg}kg")
print(f"38945g into ounce is : {ounce}ounce")

'''
How to get value from user as input
'''

userinput = float(input("Please enter the value in f: "))

f = userinput
c = (f - 32)*(5/9)
k = c + 273.15
print("f:",f,"c:",c,"k:",k)