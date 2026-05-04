import random

# Snakes and Ladders positions
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

# Player positions
player1_pos = 0
player2_pos = 0

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice):
    position += dice
    
    if position > 100:
        return position - dice  # stay if exceeds 100

    # Check for snakes
    if position in snakes:
        print(f"Oops! 🐍 Snake at {position}, go down to {snakes[position]}")
        position = snakes[position]

    # Check for ladders
    elif position in ladders:
        print(f"Yay! 🪜 Ladder at {position}, climb up to {ladders[position]}")
        position = ladders[position]

    return position

# Game loop
while True:
    input("\nPlayer 1, press Enter to roll dice...")
    dice = roll_dice()
    print(f"Player 1 rolled: {dice}")
    player1_pos = move_player(player1_pos, dice)
    print(f"Player 1 position: {player1_pos}")

    if player1_pos == 100:
        print("🎉 Player 1 wins!")
        break

    input("\nPlayer 2, press Enter to roll dice...")
    dice = roll_dice()
    print(f"Player 2 rolled: {dice}")
    player2_pos = move_player(player2_pos, dice)
    print(f"Player 2 position: {player2_pos}")

    if player2_pos == 100:
        print("🎉 Player 2 wins!")
        break