# Sample Python script.
# Press ⌃R to execute it or replace it with your code.
#import pdb; pdb.set_trace()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__mains__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# =========================================================================
# =========================================================================

#LESSON 1:  Variables and assignments
x = 5
float_value = 4.2
y = x

# Adding
summation = x+float_value

# output :: Use comma to output with string
print("\nThe adding example is: ", summation)


# Strings - use quotation, use can also add name+name
name = "Jesse"
print("The output string example is: " +name)



# LESSON 2: Formatting String :: use the f string to embed the variable

myName = "Obinna"
greeting = f"Hi {myName}"

print("The formatting string output is:", greeting)
#breakpoint()
myName = "Jesse"
print(f"Updated formatting, {myName}")    # Better practice

# Format function

make = "Ford {}"                           # Adding curly bracelets allows you to pass another variable.
model = "Mustang"
car = make.format(model)
print("Using the Format Function, output is: ", car)

# LESSON 3: User Input

name = input("\nEnter your name: ")           # Uses input keyword
print(f"\n Ututu omma {name}!")
#print(name, "\n")


# For math equations
height_input = input("\n Enter your height: ")
height = int(height_input)
reduced_height = height / 50
print(f"\n Your height divided by 5 is: {reduced_height} feet.\n")


# LESSON 4: First App :: Ask user for age, then output the months

# Have input that prompts for age
# Create a variable for months - which takes input and multiplies it by 12
# Have output statement that outputs month variable
# Use f formatting to show both values

age_prompt = input("Please enter your age: ")
age_in_months = int(age_prompt)*12
#output = ()
print(f"\nYour age in years is: {age_prompt} and your age in Months is: {age_in_months} months.")

# More refactored approach ----> refactored_age_prompt = int(input("Please enter your age"))


# LESSON 5: Lists Tuples and Sets