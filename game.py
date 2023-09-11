import time
import random

def story_intro():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroads.")
    time.sleep(1)
    print("You can go left, right, straight ahead, up the hill, or down into the valley. Which path will you choose?")
    choice = input("Enter 'left,' 'right,' 'straight,' 'up,' or 'down': ").lower()
    
    if choice == "left":
        path_left()
    elif choice == "right":
        path_right()
    elif choice == "straight":
        path_straight()
    elif choice == "up":
        path_up()
    elif choice == "down":
        path_down()
    else:
        print("Invalid choice. Please enter 'left,' 'right,' 'straight,' 'up,' or 'down'.")
        story_intro()

def path_left():
    print("You chose the left path.")
    time.sleep(1)
    event = random.randint(1, 3)  # Random event generator
    if event == 1:
        print("You encounter a friendly squirrel who leads you to a hidden treasure chest.")
        time.sleep(1)
        print("Congratulations! You've found the treasure!")
    else:
        print("You encounter a group of travelers who share their food with you.")
        time.sleep(1)
        print("You make new friends and continue your adventure together.")

def path_right():
    print("You chose the right path.")
    time.sleep(1)
    event = random.randint(1, 3)  # Random event generator
    if event == 1:
        print("You stumble into a dark cave.")
        time.sleep(1)
        print("It's too dark to see anything...")
        time.sleep(1)
        print("Game Over. You are lost in the cave.")
    else:
        print("You discover a hidden path that leads to a beautiful garden.")
        time.sleep(1)
        print("You take a moment to enjoy the peaceful surroundings before continuing your journey.")

def path_straight():
    print("You chose the path straight ahead.")
    time.sleep(1)
    event = random.randint(1, 3)  # Random event generator
    if event == 1:
        print("You come across a river with a small boat.")
        time.sleep(1)
        print("You successfully row across the river and continue your adventure.")
    else:
        print("A sudden rainstorm forces you to take shelter in a nearby cave.")
        time.sleep(1)
        print("You spend some time exploring the cave and find a hidden passage.")
        time.sleep(1)
        print("The passage leads you to a new and exciting part of the adventure.")

def path_up():
    print("You chose to climb up the hill.")
    time.sleep(1)
    event = random.randint(1, 3)  # Random event generator
    if event == 1:
        print("From the hilltop, you have a stunning view of the surrounding landscape.")
        time.sleep(1)
        print("You take a moment to enjoy the scenery and then continue your journey.")
    else:
        print("As you climb the hill, you stumble upon an old map.")
        time.sleep(1)
        print("The map reveals the location of a hidden treasure!")
        time.sleep(1)
        print("You follow the map and uncover the treasure.")

def path_down():
    print("You chose to descend into the valley.")
    time.sleep(1)
    event = random.randint(1, 3)  # Random event generator
    if event == 1:
        print("You find a peaceful meadow with colorful flowers.")
        time.sleep(1)
        print("You spend some time relaxing in the meadow before continuing your adventure.")
    else:
        print("You enter a dense forest and discover a friendly group of animals.")
        time.sleep(1)
        print("The animals offer you guidance and lead you to a hidden clearing with a magical fountain.")
        time.sleep(1)
        print("You drink from the fountain and feel refreshed, ready for new adventures.")

if __name__ == "__main__":
    story_intro()
