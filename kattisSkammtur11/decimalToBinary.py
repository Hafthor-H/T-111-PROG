

def decimal_to_binary(decimal):
    binaryList = []
    while True:
            quotentAndRemindaer = divmod(decimal,2)
            if quotentAndRemindaer[0] == 0:
                binaryList.append(quotentAndRemindaer[1])
                binaryList.reverse()
                for i in binaryList:
                     print(i,end="")
                break
            else:
                binaryList.append(quotentAndRemindaer[1])
                decimal = quotentAndRemindaer[0]
    return ""
    
decimal_to_binary(8)