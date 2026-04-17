import random
import time

print("Welcome to Niwit !")
print("Enter help for what you can do")

while True:
    user_input = input("Niwit>")

    if user_input == "help":
        print("roll-dice - rolls a dice")
        print("touch-grass - makes you touch grass")
        print("about - shows about Niwit")
        print("exit - exits Niwit")
    
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
    
    elif user_input == "exit":
        if random.randint(1, 4) == 1:
            print("See You Next Time !")
        if random.randint(1, 4) == 2:
            print("Goodbye !")
        if random.randint(1, 4) == 3:
            print("Hope you come back ! one day...")
        if random.randint(1, 4) == 4:
            print("Bye !")
        time.sleep(1)
        break

    elif user_input == "67":
        print("Bro... you really want to do it ? Y/N")
        sise_input = input("Y/N>")
        if sise_input == "Y":
            sise_while = 67
            while True:
                print("67")
                time.sleep(0.1)
                sise_while -= 1
                if sise_while == 0:
                    break
        if sise_input == "N":
            print("thanks")
            break
    else:
        print("Unknown Command")
