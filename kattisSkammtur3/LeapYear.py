year = int(input())

if(year % 4):
    print("False")
else:
    if(year % 100):
        print("True")
    else:
        if(year % 400):
            print("False")
        else:
            print("True")
