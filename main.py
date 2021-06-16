import random
foods = ['sushi', 'katsu', 'donburi', 'natto']
#randomly chooses food from list
a = random.randint(0, len(foods)-1)

print(foods[a])
#lets the user input any food into the fridge
while True:
    foodaddition = str(input("Enter foods you want to put on the fridge (or press Q if you had enough :)): "))
    if str(foodaddition).upper() == "C":
        print(foods)
    elif str(foodaddition).upper() == "Q":
        break
    else:
        foods.append(foodaddition)
print(foods[a])
# Lets the user takes out any food in the fridge
while True:
    # Ask for foods
    foodaddition = str(input(
        "Enter foods you want to take out of the fridge (or press Q if you had enough :)) (please note that there must be at least one item in the Fridge): "))
    if str(foodaddition).upper() == "C":
        print(foods)
    elif str(foodaddition).upper() == "Q" or len(foods) == 1:
        break

    # Check if present, then remove it
    elif foodaddition in foods:
        foods.remove(foodaddition)
    else:
        print("Item not in fridge")

print(foods)
print(foods[a])




