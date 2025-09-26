n = int(input())
guests = set()

for i in range(n):
    ask = input()
    name = ask[2:]
    if ask[0] == "?":
        if name in guests:
            print("Jebb")
        else:
            print("Neibb")
    elif ask[0] == "+":
        guests.add(name)
    elif ask[0] == "-":
        guests.remove(name)