number = int(input())

def sum_of_n(num):
    summa = 0
    if num <= 0:
        for i in range(num,2):
            summa += i
        print(summa)
    else:
        for i in range(num+1):
            summa += i
        print(summa)

sum_of_n(number)