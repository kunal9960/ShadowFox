# 1. Using a for loop, simulate rolling a six sided die multiple times (at least 20 times).

import random
num_6 = 0
num_1 = 0
num_two_6s_in_a_row = 0
prev_roll = None

num_rolls = 20
for _ in range(num_rolls):
    # Roll the die
    roll = random.randint(1, 6)

    # Count the rolls of 6 and 1
    if roll == 6:
        num_6 += 1
        if prev_roll == 6:
            num_two_6s_in_a_row += 1
    elif roll == 1:
        num_1 += 1

    # Update the previous roll
    prev_roll = roll


print("Number of times rolled a 6:", num_6)
print("Number of times rolled a 1:", num_1)
print("Number of times rolled two 6s in a row:", num_two_6s_in_a_row)


# 2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.

remaining_jumping_jacks = 100

while remaining_jumping_jacks > 0:
    # Perform 10 jumping jacks
    if remaining_jumping_jacks >= 10:
        completed_jacks = 10
        remaining_jumping_jacks -= 10
    else:
        completed_jacks = remaining_jumping_jacks
        remaining_jumping_jacks = 0

    print(f"Performed {completed_jacks} jumping jacks.")

    # Check if the user is tired
    tired = input("Are you tired? (yes/no): ").lower()
    if tired == "yes" or tired == "y":
        skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip_remaining == "yes" or skip_remaining == "y":
            break
    else:
        print(f"{remaining_jumping_jacks} jumping jacks remaining.")

if remaining_jumping_jacks == 0:
    print("Congratulations! You completed the workout.")
else:
    print(f"You completed a total of {100 - remaining_jumping_jacks} jumping jacks.")
