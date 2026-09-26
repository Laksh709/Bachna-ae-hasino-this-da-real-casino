import slot_machine2 as game_1
import Roulette as game_2
import time
def Start_game():
    print(r'''
╔═══════════════════════ ♠ ♥ ♦ ♣ ════════════════════════╗
║                                                        ║
║  --Welcome to the Casino!! Ready to try your luck??--  ║
║                                                        ║
╚═══════════════════════ ♣ ♦ ♥ ♠ ════════════════════════╝
''')
    
 
    print(r'''
 ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣ 
 
   _____           _____ _____ _   _  ____  
  / ____|   /\    / ____|_   _| \ | |/ __ \ 
 | |       /  \  | (___   | | |  \| | |  | |
 | |      / /\ \  \___ \  | | | . ` | |  | |
 | |____ / ____ \ ____) |_| |_| |\  | |__| |
  \_____/_/    \_\_____/|_____|_| \_|\____/ 

 ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣  ♠ ♥ ♦ ♣
''')
    print(r'''
╭─────────────────────────────────────────────────────────────╮
│                                                             │
│  [!] DISCLAIMER: All the users should be aware of the rules │
│      and the organisation is not responsible for financial  │
│      or any other personal losses.                          │
│                                                             │
╰─────────────────────────────────────────────────────────────╯
''')
    while True:
        print("\nHere are your choices for the games:")
        print(" 1) Slot Machine")
        print(" 2) Roulette")
        print(" 3) Leave Casino")
        
        try:
            choice = int(input("\nEnter Your preferred choice of game (1-3): "))
            
            if choice == 1:
                print("\nYou have chosen to play the slot machine. The game is starting....")
                time.sleep(2)
                print("The arena is all yours. Enjoy your time spent here!!")
                game_1.main()
            elif choice == 2:
                print("\nYou have chosen to play the Roulette. The game is starting....")
                time.sleep(2)
                print("The arena is all yours. Enjoy your time spent here!!")
                game_2.play()
            elif choice == 3:
                print("\nThanks for visiting the Casino. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
                
        except ValueError:
            print("\nInvalid input! Please type a number.")

if __name__ == "__main__":
    Start_game()
              
