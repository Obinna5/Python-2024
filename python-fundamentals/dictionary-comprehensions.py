# DICTIONARY COMPREHENSION

# Create users
users = [

(0, "Lokoum", "Osman"),
(1, "Papa", "Mensah"),
(2, "Nana", "Fordjour")

]

mapping_example = {user[1]: user for user in users}

#print(mapping_example)
print(mapping_example[Papa])


# Unpackcing and mapping: This will distribute the user data amongst the three variables
_, username, password = mapping_example



