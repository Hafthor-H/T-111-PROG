file_name = input()

with open("/src/" + file_name, "r") as file_in:
    for line in file_in:
        line = line.split()
        for i in line:
            print(i[::-1], end=" ")
        print()