import random
import time

print("Welcome to Niwit !")
print("Enter help for what you can do")

while True:
    user_input = input("Niwit>")

    if user_input == "help":
        print("roll-dice - rolls a dice")
        print("touch-grass - makes you touch grass")
    elif user_input == "roll-dice":
        print(random.randint(1, 6))
    elif user_input == "touch-grass":
        print("You touched grass!")
        time.sleep(5)
        print("You really thought you would get away with that ?")
        time.sleep(2)
        print("Type touch-grass in a pathetic open-source program ?")
        time.sleep(2)
        print("Now go touch some grass IRL")
        time.sleep(2)
        break
    else:
        print("Unknown Command")
