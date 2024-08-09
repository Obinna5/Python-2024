# LESSON: FOR LOOP


friends = ["Ian","Nate", "Papa", "Lokoum"]

for friend in friends:              # Use the semi-colons
    print(f"\n{friend} is my friend. \n")


# Calculate average grade

grades = [35, 43, 23 , 12, 24, 35]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total/amount)

# Can also use total = sum(grades)
