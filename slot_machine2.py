import random
import time
import os

# Symbols used in the game
SYMBOLS = ["🍒", "🍉", "🍋", "🔔", "⭐"]
FRUIT_SYMBOLS = ["🍒", "🍉", "🍋"]

def clear_screen():
    """Clears the console screen for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    """Displays the game title with a box border."""
    print("╔══════════════════════════════════╗")
    print("║    ⭐⭐ SLOT MACHINE ⭐⭐        ║")
    print("╚══════════════════════════════════╝")
    print()

def get_bet(balance):
    """Asks the user for a valid bet amount."""
    while True:
        print(f"Current Balance: {balance} coins")
        try:
            bet_input = input("Enter your bet amount: ")
            bet = int(bet_input)
            
            if bet <= 0:
                print("Invalid amount! Bet must be greater than 0.\n")
            elif bet > balance:
                print("Insufficient funds! You cannot bet more than your balance.\n")
            else:
                return bet
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

def spin_reels():
    """Simulates the spinning of the reels with a brief text animation."""
    print("\nSpinning...")
    
    # Spin animation loop
    for _ in range(5):
        s1, s2, s3 = random.choice(SYMBOLS), random.choice(SYMBOLS), random.choice(SYMBOLS)
        # Using carriage return \r to overwrite the line on the same line
        print(f"{s1} | {s2} | {s3}   ", end="\r")
        time.sleep(0.3)
        
    # Final outcome
    final_reels = [random.choice(SYMBOLS) for _ in range(3)]
    # Overwrite the last spin frame with the final result
    print(f"{final_reels[0]} | {final_reels[1]} | {final_reels[2]}   ")
    return final_reels

def calculate_winnings(reels, bet):
    """Calculates the payout based on the reel combination."""
    r1, r2, r3 = reels
    
    # Check for 3 matching symbols
    if r1 == r2 == r3:
        if r1 == "⭐":
            return bet * 15
        elif r1 == "🔔":
            return bet * 10
        elif r1 in FRUIT_SYMBOLS:
            return bet * 5
            

        
    # No matches - player loses
    return 0

def display_result(winnings, bet):
    """Displays whether the player won or lost this round."""
    print("-" * 36)
    if winnings > 0:
        print("🎉 WINNER! 🎉")
        print(f"You won {winnings} coins!")
    else:
        print("🥸 No match!")
        print(f"You lost {bet} coins.")
    print("-" * 36 + "\n")

def main():
    """Main game loop."""
    balance = 1000
    
    # Clear screen once at the beginning
    clear_screen()
    
    while balance > 0:
        display_title()
        
        # 1. Get user bet
        bet = get_bet(balance)
        
        # Deduct bet from balance immediately
        balance -= bet
        
        # 2. Spin the reels
        reels = spin_reels()
        
        # 3. Calculate winnings
        winnings = calculate_winnings(reels, bet)
        
        # Add winnings back to balance (if any)
        balance += winnings
        
        # 4. Display results
        display_result(winnings, bet)
        
        # 5. Check if game is over
        if balance <= 0:
            print("╔══════════════════════════════════╗")
            print("║          GAME OVER!              ║")
            print("║      You ran out of coins.       ║")
            print("╚══════════════════════════════════╝")
            break
            
        # 6. Ask to play again
        while True:
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again in ('y', 'n'):
                break
            print("Invalid input. Please enter 'y' or 'n'.")
            
        if play_again == 'n':
            print(f"\nThanks for playing! You are walking away with {balance} coins.")
            break
            
        # Clear the screen for the next round
        clear_screen()

if __name__ == "__main__":
    main()