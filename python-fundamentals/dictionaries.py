# LESSON: DICTIONARIES

# Key Value-pairs : Strings and Integers


friends = {"Jesse": 5, "Ian":4, "Papa": 3}          #Strings separated by 


print(friends["Jesse"])                 #Use subscript notation to access


# Adding keys
friends["Nana"] = 2
print(f"\n {friends}")

#Iterating over a 
for friend, favnums in friends.items():
    print(f"{friends}: {favnums}")      # User subscript notation to access fav number

# List of dictionaries
friends2 = [
    {"name": "Jesse", "age": 5},            # Separated by commas inside and out 
    {"name": "Ian", "age": 4},  
    {"name": "Papa", "age":3},  
    ]


# Needs to be accessed through index

print(friends2[1]["name"])

