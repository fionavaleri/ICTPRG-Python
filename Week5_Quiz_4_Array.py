# Write a program that enters a string containing a person's full name and then output their initials. Example:
# Full Name: Lachlan van der Velden
# Initials: LVDV

# Full Name: Dave Verg Douglas
# Initials: DVD

name = input("Please enter your full name: ")
initials = name.split()

print("Full Name: " + name + "\n" + "Initials: " + "".join(letter[0] for letter in initials))