# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#animal = Lion 
animal = "Lion" #Syntax error: Assigning a string without putting the quotation marks 
animal_type = "cub"
number_of_teeth = 16
#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
full_spec = "This is a {}. It is a {} and it has {} teeth".format(animal, animal_type, number_of_teeth) #Logical error: Using the f-string in an incorrect way

#print full_spec
print(full_spec) #Syntax error: Missing parentheses
