import random
counter = 0
rnum = random.randint(1,1000)

while True:
    if(counter == 10):
        break
    guess = int(input(""))
    if(guess == rnum):
        print("correct")
    elif(guess < rnum):
        print("higher")
        counter += 1
    elif(guess > rnum):
        print("lower")
        counter += 1
