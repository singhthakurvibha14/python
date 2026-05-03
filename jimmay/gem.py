import random

print("🎮 Welcome to Hide and Seek Game!")

# Computer hides at a random number
hidden_spot = random.randint(1, 20)

attempts = 0

while True:
    guess = int(input("Guess where I am hiding (1 to 20): "))
    attempts += 1

    if guess < hidden_spot:
        print("📉 Too low! Try again.")
    elif guess > hidden_spot:
        print("📈 Too high! Try again.")
    else:
        print(f"🎉 You found me in {attempts} attempts!")
        break

print("Game Over!")