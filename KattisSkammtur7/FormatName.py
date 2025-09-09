firstName, lastName = input("").split(",")

firstInitaial = firstName[:1].upper()
lastInital = lastName[:2].upper() + "."
firstName = firstInitaial+firstName[1:]
print(lastInital, firstName)

