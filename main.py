import pet
import time
"""
- This is a simple pet simulator program that allows users to create a pet and interact with it.
- The user can feed the pet, play with it, teach it tricks, and check its status.
- The program uses a class to represent the pet and its attributes, and it provides a simple text-based interface for user interaction.
- The program is designed to be easy to use and understand, making it suitable for beginners in programming.
- The program is written in Python and uses basic programming concepts such as classes, methods, and user input.
- The program is designed to be run in a terminal or command prompt, and it provides clear instructions for the user to follow.
"""

from pet import Pet

def main():
    pet = Pet("Buddy") 
    
    print("\nWelcome to your digital pet game!")
    print(f"You're now taking care of Buddy.\n")

    while True:

        pet.get_status()
        
        print("Choose an action:")
        actions = [
            "1. Eat",
            "2. Sleep",
            "3. Play",
            "4. Train a new trick",
            "5. Show tricks",
            "6. Quit"
        ]
        print("\n".join(actions))
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            trick = input("sit, rollover: ")
            tricks = [trick.strip() for trick in
                      tricks_input.split(',')]
        
            for trick in tricks:
             if trick:  
                pet.train(trick)
        elif choice == '5':
            pet.show_tricks()
        elif choice == '6':
            print(f"\nGoodbye! Buddy will miss you!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
        
        print("\n" + "-"*30)  

if __name__ == "__main__":
    main()
