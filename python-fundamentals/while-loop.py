#LESSON: WHILE-LOOP

number = 5

while True:
    user_input = input("Wanna play? (y/n)")

    if user_input =="n":
        break

    user_number = int(input("Guss the number: "))
    if user_number == number:
        print("Correct!")
    elif abs(number -user_input) == 1:                  # Absolute funtion
        print("You were off by one.")
    else:
        print("Sorry, its wrong!")
