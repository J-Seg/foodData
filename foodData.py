Food = []
Location = []

filename = 'Food & Storage.txt' #file whre info is stored
foodStorage = True

while foodStorage == True:
    #adding food and location info 
    print("Please enter the food you want to store: ")
    food = input()
    Food.append(food)

    with open(filename, 'a') as file_object:
        file_object.write(food)

    print("Now please enter the location of where the food is: ")
    location = input()
    Location.append(location)

    with open(filename, 'a') as file_object:
        file_object.write(location)

    response = input("Would you like to add more food? (Y/N) ")
    if response == 'N' or 'n':
        foodStorage = False
    elif response == 'Y' or 'y':
        foodStorage == True

#what and where food is stored
print("\n--- Food and Where ---")
print("Food: ", Food)
print("Location: ", Location)