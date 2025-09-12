email = input()

emailLen = len(email)
atCount = email.count("@")
dotCount = email.count(".")
atPosition = email[::-1].find("@")
atPosition = emailLen - atPosition - 1 
dotPosition = email[::-1].find(".")
dotPosition = emailLen - dotPosition -1

if "@" in email:
    if email[0] == ".":
         print("Email address starts with a dot.")
    elif atCount > 1:
        for i in range(atPosition):
            print(" ", end="")
        print("^--there is an extra @ symbol here.")  
    elif atPosition == 0:
            print("There is nothing before the @ symbol.")
    elif atPosition == emailLen-1:
         for i in range(atPosition):
              print(" ",end="")
         print("^--there is nothing after the @ symbol.")
    elif dotCount > 1:
        for i in range(dotPosition): 
              print(" ", end="")
        print("^--there is an extra dot here.")
else:
    print("@ symbol is missing.")