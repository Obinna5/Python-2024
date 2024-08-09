# Object-Oriented Programming and Classes


class Runners:                   # Class creation
    def __init__(self):          # self is just a variable name
      self.name = "Shakari"      # define class name values

    def fname(self):            # function that returns first name
       return self.name


runner = Runners()              # Object creation

print(runner.name)              # First way to print a name


sprinter = {"name":"Usain", "Sprint times": (10, 12.1, 11.1)}   # Set that has a tuple within

def average_sprint(sequence):  # Function for calculating average
    return sum(sequence)/len(sequence)

print(average_sprint(sprinter["Sprint times"])) # Convention

print(runner.fname())         # Second way to print


