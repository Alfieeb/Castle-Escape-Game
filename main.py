import time

space = "                             "

def wait():
    time.sleep(1.5)

playerHealth = 10
Inventory = []

def gameSetup():
    


    print("=============")
    print("CASTLE ESCAPE")
    print("=============")
    print(space)
    wait

    playerName = input("Enter your player's name. ")
    print(f"Welcome to castle escape {playerName}!")
    print(space)
    wait()

    print("You awaken in the castle dungeon, chained and trapped. You need to find a way out…")
    print(space)
    wait()
    print("But escaping isn’t enough — the crown jewels still await your grasp.")
    print(space)
    wait()
    print("The air is damp and cold, and distant footsteps echo through the stone halls.")
    print(space)
    wait()
    print("Somewhere above, guards patrol, unaware of your daring plan.")
    print(space)
    wait()

def dungeonRoom():
    ActionOne = ""
    while True:  # infinite loop until break manually
        ActionOne = input("Would you like to look around for now Y/N? ")
        if ActionOne.upper() == "Y":
            print("You spot the heavy dungeon lock securing the door.")
            print(space)
            wait()
            print("A loose rock lies on the floor — maybe it could be useful.")
            print(space)
            wait()
            print("From above, you hear footsteps echoing through the stone halls.")
            print(space)
            wait()
            break  # exit loop
        elif ActionOne.upper() == "N":
            print("You decide to stay put for now, listening to the footsteps above.")
            break  # exit loop
        else:
            print("Please enter Y or N")

    ActionTwo = ""
    while True:
        ActionTwo = input("Do you want to pick up a loose rock, Y/N? ")
        print(space)
        wait()

        if ActionTwo.upper() == "Y":
            Inventory.append("Rock")
            print("You pick up the rock — maybe it can help break the lock.")
            print(space)
            wait()
            break
        elif ActionTwo.upper() == "N":
            print("You leave the rock on the floor for now.")
            break
        else:
            print("Please enter Y or N")


dungeonRoom()