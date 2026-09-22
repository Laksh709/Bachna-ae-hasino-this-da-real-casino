import random
import time 
def play():
    print("\n--- Welcome to the Roulette!Ready to test your luck?! ---")
    print("Disclamer : All the users should be aware of the rules and the organisation is " \
    "not respobnsible for financial or any other personal losses")
    print("These are the available bets for you: \n Straight up \n Red or Black\n Odd even ")
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
    Bet_type = input("Enter your prefferd type of bet you are wiilling to do : ")

    def straight_up():
        print("""
      ___            _     _   _       
     | _ \___ _  _  | |___| |_| |_ ___ 
     |   / _ \ || | | / -_)  _|  _/ -_)
     |_|_\___/\_,_| |_\___|\__|\__\___|
    """)
        print("--You have choosen straight up. Welcome")
        bet = int(input("Enter your preffered numbber between 0 and 36 both included"))
        cash = int(input("Enter the amount you need to bet on "))
        print("The dealer spins the wheel...")
        time.sleep(1.5)
        num = random.randint(0,36)
        print("The ball is bouncing...")
        time.sleep(1.5)
        print(f"It landed on {num}!")
        if num == bet:
            winnings = cash*35 + cash
            print(random.choice(win_messages))
            print(f"Your price is {winnings} $ ")
            return winnings
        else:
            print(random.choice(lose_messages))
            return 0
    def red_black():
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
            winnings_1 = cash_1*2
            print(f"Yeahhh,the colour is {color}")
            print(random.choice(win_messages))
            print(f"Your price is {winnings_1} $ ")
            return winnings_1
        else:
            print(f"Ohh,the color was {color}")
            print(random.choice(lose_messages))
            return 0


    if Bet_type== "Straight up":
        straight_up()
    elif Bet_type== "Red or Black":
        red_black()
    
play()        


 