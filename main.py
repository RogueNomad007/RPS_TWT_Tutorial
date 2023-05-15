import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
probability_picks = [0, 1, 2]
i = 2

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit").lower()
    if user_input == "q":
        break

    if user_input not in options:
        i -= 1
        continue

    random_number = random.randint(0,i)
    # R = 0, P = 1, S = 2
    temp_pick = probability_picks[random_number]
    computer_pick = options[temp_pick]
    print("The computer picked:", computer_pick)

    if user_input == computer_pick:
        print("You Drew!")
        if user_input == "rock":
            probability_picks.append(1)
        elif user_input == "paper":
            probability_picks.append(2)
        else:
            probability_picks.append(0)

    elif user_input == "rock" and computer_pick == "scissors":
        print("You Win!")
        user_wins += 1
        probability_picks.append(1)

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_wins += 1
        probability_picks.append(2)

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Win!")
        user_wins += 1
        probability_picks.append(0)

    else:
        print("You Lost!")
        computer_wins += 1
        if user_input == "rock":
            probability_picks.append(1)
        elif user_input == "paper":
            probability_picks.append(2)
        else:
            probability_picks.append(0)
    print("You won ",user_wins, " times!")
    print("The computer won ",computer_wins, " times!")
    print(probability_picks)
    i += 1

print("Goodbye")