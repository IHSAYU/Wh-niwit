import random

print("Welcome to Niwit !")
print("Enter help for what you can do")

while True:
    user_input = input("Niwit>")

    if user_input == "help":
        print("roll-dice - rolls a dice")
    elif user_input == "roll-dice":
        print(random.randint(1, 6))
