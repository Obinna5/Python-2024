
# LESSON : LISTS TUPLES & SETS

list = ["Jesse", "Obinna", "Brown"] # Can be modified and Keeps the order
tuples = ("Amma", "Awura")# Tuples can't be modified (added or remvoed)
set = {"Chi","Anaele","Brown"}  # Can be modified || Cannot have dupes in sets and is not ordered

#Subscript notation output
print(f"\n {list[2]}")

# Appending
list.append("Nkem")

#Removing
list.remove("Nkem")

#Adding 
set.add("Dad :)")

list.append("Nkem")
print(f"\n {set} \n")
print(f"\n {list} \n")

richmond = {"Ian","Papa", "Nana"}
dumfries = {"Ian","Nate", "Chuks"}

#Take one set and remove elements > Subject against the comparision
local_friends = dumfries.difference(richmond)
print(local_friends) # Output Chuks and nate

# Union - Combine the two
union_friends = richmond.union(dumfries)
print(f"\n {union_friends}")

# Intersect 
both = richmond.intersection(dumfries)
print(f"\n {both}")
