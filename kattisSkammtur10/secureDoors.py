n = int(input(""))

inside = set()

for i in range(n):
    movement = input("")
    splitMove = movement.split()
    if "entry" in movement:
        if splitMove[1] in inside:
            print(splitMove[1], "entered (ANOMALY)")
        else:
            inside.add(splitMove[1])
            print(splitMove[1], "entered")
    elif "exit" in movement:
        if splitMove[1] in inside:
            inside.remove(splitMove[1])
            print(splitMove[1], "exited")
        else: 
            print(splitMove[1], "exited (ANOMALY)")