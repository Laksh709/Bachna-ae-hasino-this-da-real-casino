import random
def play():
    print("\n--- Welcome to the Roulette!Ready to test your luck?! ---")
    print("Disclamer : All the users should be aware of the rules and the organisation is " \
    "not respobnsible for financial or any other personal losses")
    print("These are the available bets for you: \n Straight up \n Red or Black\n Odd even ")

    Bet_type = input("Enter your prefferd type of bet you are wiilling to do : ")
    def straight_up():
        
        print("--You have choosen straight up. Welcome")
        bet = int(input("Enter your preffered numbber between 0 and 36 both included"))
        cash = int(input("Enter the amount you need to bet on "))
        num = random.randint(0,36)
        print(num)
        if num == bet:
            winnings = cash*35 + cash 
            print(f"Wohoo!! You have won the game,your price is {winnings} $ ")
            return winnings
        else:
            print("Aw, you lost this time. Better luck on the next spin!")
            return 0
    if Bet_type== "Straight up":
        straight_up()
    
play()        


 