import random 

snakesAndLadderPos = []
player1Pos = 0
player2Pos = 0

def initialize() -> None:
    """Ensure that games play out deterministically by specifying the random seed.

    This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in the autograder.
    """
    random.seed(1337)

def rollDice():
    return random.randint(1,6)

def laddersAndSnakes(s, e):
    snakesAndLadderPos.append([s,e])

def checkForLorS(position):
    global snakesAndLadderPos
    snakesAndLadderPos = sorted(snakesAndLadderPos, key=lambda x: x[0])
    for i in snakesAndLadderPos:
        if i[0] == position:
            position = i[1]
    return position


def main():
    initialize()
    global player1Pos
    global player2Pos
    n = int(input())
    for i in range(n):
        start, stop = input().split(" ")
        laddersAndSnakes(int(start),int(stop))
    player1 = input("")
    player2 = input("")

    while True:
        player1Dice = rollDice()
        player1Pos += player1Dice
        player2Dice = rollDice()
        player2Pos += player2Dice
        
        if player2Pos >= 100:
            print(f"{player2} won the game.")
            break
        print(f"{player1} rolled {player1Dice} and is now at square {player1Pos}.")
        newP1Pos = checkForLorS(player1Pos)
        if newP1Pos != player1Pos:
            if newP1Pos > player1Pos:
                print(f"Splendid! {player1} climbed a ladder up to square {newP1Pos}.")
                player1Pos = newP1Pos
            else:
                print(f"Darn! A snake brought {player1} down to square {newP1Pos}.")
                player1Pos = newP1Pos
        if player1Dice == 6:
            continue
        else:
            if player1Pos >= 100:
                print(f"{player1} won the game.")
                break
            print(f"{player2} rolled {player2Dice} and is now at square {player2Pos}.")
            newP2Pos = checkForLorS(player2Pos)
            if newP2Pos != player2Pos:
                if newP2Pos > player2Pos:
                    print(f"Splendid! {player2} climbed a ladder up to square {newP2Pos}.")
                    player2Pos = newP2Pos
                else:
                    print(f"Darn! A snake brought {player2} down to square {newP2Pos}.")
                    player2Pos = newP2Pos
main()
