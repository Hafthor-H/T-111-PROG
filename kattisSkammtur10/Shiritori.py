#Óklárað

n = int(input(""))

p1Flag = True
p2Flag = True

counter = 0
for i in range(n):
    player1 = input("")
    counter += 1
    if counter == n:
        break
    player2 = input("")
    counter += 1
    player1Len = len(player1) - 1 
    player2Len = len(player2) - 1 
    if player2[0] != player1[player1Len]:
        p2Flag = False
    elif player1[0] != player2[player2Len]:
        p1Flag = False

if p1Flag and p2Flag:
    print("Fair Game")
elif not p1Flag:
    print("Player 1 lost")
elif not p2Flag:
    print("Player 2 lost")