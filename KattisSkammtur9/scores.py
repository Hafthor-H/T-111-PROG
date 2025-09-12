nums = input().split()
sumList = []
if len(nums) < 3:
    print("At least 3 scores needed!")
else:
    for i in range(len(nums)):
        floatNum = float(nums[i])
        sumList.append(floatNum)
    sumList.sort()
    sumList = sumList[3:]

    sumOfNums = sum(sumList)
    print("Sum of scores (3 lowest removed): {}".format(float(sumOfNums)))

