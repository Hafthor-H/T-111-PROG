n, m = input("").split()
megaString = ""
sum = 0

yarn = {
    ".": 20,
    "O": 10,
    "\\": 25,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22
}
for i in range(int(n)):
    megaString += input("")

for k in megaString:
    if k in yarn.keys():
        sum += yarn.get(k)
print(sum)