import random

def play_game():
    secret_number = random.randint(1, 100)
    guesses = 0
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess < secret_number:
                print("📈 Too low! Try higher.")
            elif guess > secret_number:
                print("📉 Too high! Try lower.")
            else:
                print(f"🎊 Correct!  You got it in {guesses} guesses!")
                break
        except ValueError:
            print("❌ Please enter a valid number!")

    return guesses  # Optional: for tracking high scores later
      
#Main game loop
while True:
    play_game()
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! 👋")
        break
