# Unpacking Arguments


def subtract(*args):                # The star allows multiple arguments in a single variable
    print(args)
    total = 0
    for arg in args:
        total -= arg

    return total

#subtract(5, 3, 1)
#print(subtract (5, 3, 1))

def add(x,y):
    return x + y

nums = [3, 5]
print(add())


def multiply(*args):
    total = 1
    for arg in args: 
        total *= arg
    
    return total

def apply(*args, operator):         # Collect all arguments into args tuple and have a named (Operator) argument at the end
    if operator == "*":
        return multiply(*args)      # Star is used to iterate through the values in the Tuple
    if operator == "+":
        return add(args)
    else: 
        return "No valid operator provided to apply ()."

print(apply(1,2,3, operator="*"))