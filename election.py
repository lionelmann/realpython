from random import random

total_A_wins = 0
total_B_wins = 0

trials = 10

for trails in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .87:
        A_win += 1
    else:
        B_win += 1
    if random() < .65:
        A_win += 1
    else:
        B_win += 1
    if random() < .17:
        A_win += 1
    else:
        B_win += 1
    # determine overall election outcome
    if A_win > B_win:
        total_A_wins += 1
    else:
        total_B_wins += 1

    print("Probability A wins:", total_A_wins / trials)
    print("Probability B wins:", total_B_wins / trials)
