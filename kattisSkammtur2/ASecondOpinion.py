timi = int(input(""))

sek = timi % 60
min = timi // 60

klst = min // 60
min = min % 60

print("{} : {} : {}".format(klst, min, sek))
