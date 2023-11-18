import random
def coin_flip():
    flips = 0
    prev = None
    streak = 0
    while streak < 3:
        r = random.random() 
        if r < 0.5:
            outcome = "H"
        else:
            outcome = "T"
        flips += 1
        print(outcome, end="")
        if outcome == prev:
            streak += 1
        else:
            streak = 1
        prev = outcome
    print()
    return flips
flips_list = []
for i in range(10):
    flips_list.append(coin_flip())
average = sum(flips_list) / len(flips_list)
print(f"The average number of flips needed is {average:.2f}")