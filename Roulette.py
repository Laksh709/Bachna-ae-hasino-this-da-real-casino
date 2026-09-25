import random
import time 

def play():
    print("\n--- Welcome to the Roulette!Ready to test your luck?! ---")
    print("Disclamer : All the users should be aware of the rules and the organisation is " \
    "not respobnsible for financial or any other personal losses")
   
    win_messages = [
    "Beginner's luck? Or are you a pro?",
    "Winner winner! Don't spend it all in one place.",
    "The dealer glares at you as he hands over your chips."
    ]
    lose_messages = [
    "Ouch. The casino thanks you for your donation.",
    "Not even close! Better luck next spin.",
    "Oof. I'll get the funny 'fahhh' sound ready for you.",
    "Another one bites the dust."
    ]
    balance = 1000
    
    print(f"Your initial balance is {balance}")
   

    def straight_up(current_balance):
        print("""
      ___            _     _   _       
     | _ \___ _  _  | |___| |_| |_ ___ 
     |   / _ \ || | | / -_)  _|  _/ -_)
     |_|_\___/\_,_| |_\___|\__|\__\___|
    """)
        print("--You have choosen straight up. Welcome")
        bet = int(input("Enter your preffered numbber between 0 and 36 both included"))
        cash = int(input("Enter the amount you need to bet on "))
        if cash > current_balance:
            print("You don't have enough chips for that bet!")
            return current_balance
        current_balance -= cash
        print("The dealer spins the wheel...")
        time.sleep(1.5)
        num = random.randint(0,36)
        print("The ball is bouncing...")
        time.sleep(1.5)
        print(f"It landed on {num}!")
        if num == bet:
            winnings = cash*35 + cash
            current_balance += winnings
            print(random.choice(win_messages))
            
        else:
            print(random.choice(lose_messages))
        return current_balance
    def red_black(current_balance):
        print("""
               ___            _     _   _       
              | _ \___ _  _  | |___| |_| |_ ___ 
              |   / _ \ || | | / -_)  _|  _/ -_)
              |_|_\___/\_,_| |_\___|\__|\__\___|
             """)

        
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        
          
        print("--You have choosen Red or Black. Welcome")
        colour  = input("Enter your choice of colour").strip().capitalize()
        cash_1 = int(input("Enter the amount you need to bet on "))
        if cash_1 > current_balance:
            print("You don't have enough chips for that bet!")
            return current_balance
            
        current_balance -= cash_1
        print("The dealer spins the wheel...")
        time.sleep(1.5)
        num_1 = random.randint(0,36)
        print("The ball is bouncing...")
        time.sleep(1.5)
        print(f"It landed on {num_1}!") 
        if num_1 == 0:
            color = "Green"
        elif num_1 in red_numbers:
            color = "Red" 
        else:
            color = "Black"
        if colour == color:
           winnings_1 = cash_1 * 2
           current_balance += winnings_1
           print(f"Yeahhh,the colour is {color}")
           print(random.choice(win_messages))
           print(f"Your price is {winnings_1} $ ")
           return winnings_1
        else:
            print(f"Ohh,the color was {color}")
            print(random.choice(lose_messages))
        return current_balance

    def odd_even(current_balance):
        print("""
                         ___            _     _   _       
                        | _ \___ _  _  | |___| |_| |_ ___ 
                        |   / _ \ || | | / -_)  _|  _/ -_)
                        |_|_\___/\_,_| |_\___|\__|\__\___|
                       """)
        print("--You have choosen Odd/even. Welcome--")
        number = input("Enter the choice of your number type").strip().capitalize()
        cash_2 = int(input("Enter the amount you need to bet on "))
        if cash_2 > current_balance:
            print("You don't have enough chips for that bet!")
            return current_balance
            
        current_balance -= cash_2
        print("The dealer spins the wheel...")
        time.sleep(1.5)
        num_2 = random.randint(0,36)
        print("The ball is bouncing...")
        time.sleep(1.5)
        print(f"It landed on {num_2}!") 
        if num_2== 0:
            print("You have lost all your money")
            print(random.choice(lose_messages))
            return current_balance
    
        elif num_2%2== 0:
            type_num = "Even"
        else:
            type_num= "Odd"
        if number == type_num:
            winnings_2 = cash_2 * 2
            current_balance += winnings_2
            print(f"Yeahhh,the type of number is {type_num}")
            print(random.choice(win_messages))
            print(f"Your price is {winnings_2} $ ")
            
        else:
            print(f"Ohh,the type of number was {type_num}")
            print(random.choice(lose_messages))
        return current_balance   

          

    while balance > 0:
        print(f"\n--- YOUR CURRENT BALANCE: ${balance} ---")
        print("Available actions: \n [1] Straight up \n [2] Red or Black \n [3] Odd or even \n [4] Withdraw & Quit")
        
       
        choice = input("Enter the number of what you want to do (1-4): ").strip()

        
        if choice == "1":
            balance = straight_up(balance)
        elif choice == "2":
            balance = red_black(balance)
        elif choice == "3":
            balance = odd_even(balance)
        elif choice == "4":
            print(f"\nCashing out... You leave the table with ${balance}.")
            break 
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            
    
    if balance <= 0:
        print("\nYou are completely out of money! The bouncers escort you out of the casino.")
play()        


 