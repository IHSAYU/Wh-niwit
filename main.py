import random
import time

print("Welcome to Niwit !")
print("Enter help for what you can do")

while True:
    user_input = input("Niwit>")

    if user_input == "help":
        print("roll-dice - rolls a dice")
        print("touch-grass - makes you touch grass")
        print("about - Shows about Niwit")
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
    elif user_input == "about":
        print("Wh-niwit")
        print("We Have No Idea What Is This")
        print("by IHSAYU, and Open-source (2026) You can come add a feature idk")
        print("https://github.com/IHSAYU/Wh-niwit")
    else:
        print("Unknown Command")
