import random
counter = 0
low = 1
high = 1000

while counter != 10:
    guess = (low + high) // 2
    print(guess, flush=True)
    kattis = input()
    if (kattis == "lower"):
        high = guess - 1
        counter += 1
    elif (kattis == "higher"):
         low = guess + 1
         counter += 1
    elif (kattis == "correct"):
        break