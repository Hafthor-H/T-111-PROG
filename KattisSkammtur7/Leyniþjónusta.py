email = input("")

newMail = ""

splits = email.split(" ")
for i in range(len(splits)):
    newMail += splits[i]
    
print(newMail)