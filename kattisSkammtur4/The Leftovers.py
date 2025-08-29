
summa = 0
while True:
    playerCount = int(input(""))
    if(playerCount >= 2):
        for i in range(playerCount):
            nums = int(input(""))
            summa += nums
        winner = summa % playerCount
        print("The sum of all contributions is ", summa)
        print("When {} is divided by {}, the remainder is {}".format(summa, playerCount, winner))
        print("Player {} is the winner!".format(winner))
        break