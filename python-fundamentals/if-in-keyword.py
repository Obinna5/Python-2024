# LESSON 9: IF and IN Keyword

colors = {"Red", "Blue", "Green"}

user_color = input("Enter your favorite color: ")

if user_color in colors:
    print(f"Your color {user_color} matched")
else:
    print("Color doesn't match")