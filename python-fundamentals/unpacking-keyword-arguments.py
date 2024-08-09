#Unpacking-keyword arguments

def named(**kwargs):
    print(kwargs)


named(name="Jesse", age=25)

print(named)            # A dictionary is crteated


def named2(name2, age2):
    print(name2, age2)

details = {"name2": "Jesse", "age2": 25}

named2(**details)


#print_nicely(**kwargs):
#named(**kwargs)
#for arg, value in kwargs.items():
#    print(f"{arg}: {value}")

#print_nicely(name="Joe", age=50)