# LESSON 16: Functions with arguments and Parameters


def subtract(x,y):
    result = x - y
    print(f"\n The results for Substraction Method is: {result}")


##subtract(5,3)

# Hard assigning arguments

def person(fname, lname):
    print(f"\n The individual you entered is: {fname} {lname} \n")

# Allows you to assign variable order
##person(lname="Ochocinco", fname="Chad")




#LESSON 17: Default Parameter values

def add(x,y=5):
    print(f"\n Add Funciton output {x+y}\n")


##add(10)


#LESSON 18: Return Values

# Use the return keyword
def multiply(a, b):
    return a*b

multi = multiply(5,5)
print(f"\nMultiply function output: {multi}\n")



# Functions : Create with "def" > Use paramaters if needed > use semi colon > Use return keyword as well as creating a new variable that holds the function. 
