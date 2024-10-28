#######################################         DAY1          ####################################### 

def readInInput(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


#######################################         DAY2          ####################################### 

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


#######################################         DAY3          ####################################### 
def checkNextNumber(line, numberIndex):
    totalInt = []
    keepGoing = True
    while keepGoing:
        if line[numberIndex].isdigit():
            totalInt.append(line[numberIndex])
            numberIndex += 1
        else:
            #print(totalInt)
            break
    return totalInt



def checkNextNumberLength(line, numberIndex):
    totalInt = []
    keepGoing = True
    while keepGoing:
        if line[numberIndex].isdigit():
            totalInt.append(line[numberIndex])
            numberIndex += 1
        else:
            #print(totalInt) 
            break

    return numberIndex

def checkNextLine(line, lowerBound, upperBound):
    print(lowerBound)
    while lowerBound < upperBound:
        #print(upperBound)
        print(line)
        print(line[lowerBound])
        if line[lowerBound] in ( '*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            print("YESSSSSS")
        lowerBound += 1
        print(lowerBound)
        print(upperBound)