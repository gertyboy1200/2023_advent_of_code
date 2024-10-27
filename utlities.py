################    DAY 1   ################
def readInInput(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

################    DAY 2   ################
def getGameNumber(gameLine):
    return int(''.join(filter(str.isdigit, gameLine[1])))

def getDiceColor(gameLine):
    a = gameLine
    q = ""
    for i in a:
        if i.isalpha():
            q = "".join([q,i])
    return q

def isValid(gameLine, colorIndex, numOfCubesIndex):
    #print(gameLine, colorIndex, numOfCubesIndex, gameLine[colorIndex], gameLine[numOfCubesIndex])
    if 'red' in gameLine[colorIndex]:
        if int(gameLine[numOfCubesIndex]) <= 12:
            return True
        else:
            return False
    elif 'blue' in gameLine[colorIndex]:
        if int(gameLine[numOfCubesIndex]) <= 14:
            return True
        else:
            return False
    elif 'green' in gameLine[colorIndex]:
        if int(gameLine[numOfCubesIndex]) <= 13:
            return True
        else:
            return False
    else:
        print("error")

################    DAY 3   ################
def checkNextNumber(line, numberIndex):
    totalInt = []
    keepGoing = True
    while keepGoing:
        checkVar = 1
        if line[numberIndex].isdigit():
            totalInt.append(line[numberIndex])
            numberIndex += 1
        else:
            print(totalInt) 
            keepGoing = False

    #print(numberIndex)
    testVar = numberIndex
    return numberIndex        