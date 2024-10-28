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
    """
    Extracts the next sequence of digits from a specified starting index in a line.

    Args:
        line (str): The string line to check.
        numberIndex (int): The starting index in `line` to begin looking for digits.

    Returns:
        int: The integer representation of the consecutive digits found starting at `numberIndex`.
    """
    totalInt = []
    keepGoing = True
    while keepGoing:
        if line[numberIndex].isdigit():
            totalInt.append(line[numberIndex])
            numberIndex += 1
        else:
            break
    return int(''.join(map(str, totalInt)))

def nextNumberLength(validInt):
    """
    Determines the number of digits in a given integer.

    Args:
        validInt (int): The integer whose length in digits is to be determined.

    Returns:
        int: The number of digits in `validInt`.
    """
    return len(str(validInt))

def checkNextNumberIndex(line, numberIndex):
    """
    Finds the ending index of a sequence of digits starting at a specified index in a line.

    Args:
        line (str): The string line to check.
        numberIndex (int): The starting index in `line` to begin looking for digits.

    Returns:
        int: The index immediately following the last digit in the sequence found starting at `numberIndex`.
    """
    totalInt = []
    keepGoing = True
    while keepGoing:
        if line[numberIndex].isdigit():
            totalInt.append(line[numberIndex])
            numberIndex += 1
        else:
            break
    return numberIndex

def checkNextLine(line, lowerBound, upperBound):
    """
    Checks if any special characters are present on the next line.

    Args:
        line (str): The string line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1

def checkPrevLine(line, lowerBound, upperBound):
    """
    Checks if any special characters are present on the previous line.

    Args:
        line (str): The string line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1

def checkLine(line, lowerBound, upperBound):
    """
    Checks if any special characters are present on the current iterating line.

    Args:
        line (str): The string line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1
