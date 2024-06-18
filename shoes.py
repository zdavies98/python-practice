# Figure out which shoes someone should wear based on their gender and location

# Ask for Input / Assign variables
gender = input("What is your gender?: ")
location = input("What is your occasion?: ")

if (location == "Gym"):
    swimming = input("Will you be swimming? (Y/N): ")
    if (swimming == "Y"):
        print("Swim shoes")
    if (swimming == "N"):
        print("Gym shoes")

#Work the magic: provide users with their appropriate shoes!
if (gender == "Male") and (location == "Casual"):
    print("Top sliders")

if (gender == "Male") and (location == "Work"):
    print("Top sliders")

if (gender == "Female") and (location == "Work"):
    print("Pumps")

if (gender == "Female") and (location == "Casual"):
    print("Flats")

if (gender == "Male") and (location == "Formal"):
    print("Oxfords")

if (gender == "Female") and (location == "Formal"):
    print("Heels")