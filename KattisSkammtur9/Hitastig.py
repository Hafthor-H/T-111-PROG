days = int(input())
heatList = []
heat = input() 

for i in heat.split():
    h = int(i)
    heatList.append(h)

print(max(heatList),end=" ")
print(min(heatList))