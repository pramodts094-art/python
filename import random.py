import random
import time

lanes = ["Left", "Middle", "Right"]
player_lane = "Middle"
score = 0

print("🚗 Welcome to Car Racing Game!")
print("Avoid the incoming cars!")
print("Controls: L = Left, M = Middle, R = Right")
print("------------------------------------")

while True:
    enemy_lane = random.choice(lanes)

    print("\nYour lane:", player_lane)
    print("Enemy car in lane:", enemy_lane)

    move = input("Move (L/M/R): ").upper()

    if move == "L":
        player_lane = "Left"
    elif move == "M":
        player_lane = "Middle"
    elif move == "R":
        player_lane = "Right"
    else:
        print("Invalid move!")

    if player_lane == enemy_lane:
        print("💥 Crash! Game Over!")
        print("Final Score:", score)
        break
    else:
        score += 1
        print("✅ Safe! Score:", score)

    time.sleep(1)
