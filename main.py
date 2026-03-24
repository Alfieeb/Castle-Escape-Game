import time

space = "                             "
wait = time.sleep(1)

def gameSetup():
    
    playerHealth = 10
    playerInventory = []

    print("=============")
    print("CASTLE ESCAPE")
    print("=============")
    print(space)
    wait

    playerName = input("Enter your player's name. ")
    print(f"Welcome to castle escape {playerName}!")
    print(space)
    wait

    print("You awaken in the castle dungeon, chained and trapped. You need to find a way out…")
    print(space)
    wait
    print("But escaping isn’t enough — the crown jewels still await your grasp.")
    print(space)
    wait
    print("The air is damp and cold, and distant footsteps echo through the stone halls.")
    print(space)
    wait
    print("Somewhere above, guards patrol, unaware of your daring plan.")
    print(space)
    wait

def dungeonRoom():
    ActionOne = ""
    while True:  # infinite loop until we break manually
        ActionOne = input("Would you like to look around for now Y/N? ")
        if ActionOne.upper() == "Y":
            print("You spot the heavy dungeon lock securing the door.")
            print("A loose rock lies on the floor — maybe it could be useful.")
            print("From above, you hear footsteps echoing through the stone halls.")
            break  # exit loop
        elif ActionOne.upper() == "N":
            print("You decide to stay put for now, listening to the footsteps above.")
            break  # exit loop
        else:
            print("Please enter Y or N")


