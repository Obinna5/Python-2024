# LESSON 19: Lambda Functions

# Lambda functions are functions with no name and is used to return values
# Used for abstraction

def add(x,y):
    return x + y

##print(f"\n Add function output: {add(5,5)}\n")


# Used to return outputs. Use the lambda keyword > Have Varaibles and logic assigned after

lambdaAdd = lambda x, y: x+y

##print(f"\n LambdaAdd Function output: {lambdaAdd(5,10)} \n")



# Passing a List into a lambda function

def double(x):
    return x * 2

sequence = [1, 3, 5, 7, 10]

# Create a variable to store > Use "List Comprehension" to pass the Double function with "x" to iterate through the List
doubled = [double(x) for x in sequence]
print(f"\n The Sequence doubled is: {doubled}\n")

# This can be done with the Map function, use List keyword to return values of a list. 
mapDoubled = list(map(double, sequence))
print(f"\n The MapDoubled output is: {mapDoubled}\n")

# Re-writing using map as a lambda funciton
lambdaMap = map(lambda x,y: x*2, sequence)
