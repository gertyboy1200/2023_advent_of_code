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

def checkNextNumber(line: list[str], numberIndex: int) -> int:
    """
    Extracts the next sequence of digits from a specified starting index in a line.

    Args:
        line (list[str]): The list of characters in the line to check.
        numberIndex (int): The starting index in `line` to begin looking for digits.

    Returns:
        int: The integer representation of the consecutive digits found starting at `numberIndex`.
    """
    totalInt = []
    while numberIndex < len(line) and line[numberIndex].isdigit():
        totalInt.append(line[numberIndex])
        numberIndex += 1
    return int(''.join(totalInt))


def nextNumberLength(validInt: int) -> int:
    """
    Determines the number of digits in a given integer.

    Args:
        validInt (int): The integer whose length in digits is to be determined.

    Returns:
        int: The number of digits in `validInt`.
    """
    return len(str(validInt))


def checkNextNumberIndex(line: list[str], numberIndex: int) -> int:
    """
    Finds the ending index of a sequence of digits starting at a specified index in a line.

    Args:
        line (list[str]): The list of characters in the line to check.
        numberIndex (int): The starting index in `line` to begin looking for digits.

    Returns:
        int: The index immediately following the last digit in the sequence found starting at `numberIndex`.
    """
    while numberIndex < len(line) and line[numberIndex].isdigit():
        numberIndex += 1
    return numberIndex


def checkNextLine(line: list[str], lowerBound: int, upperBound: int) -> bool:
    """
    Checks if any special characters are present in the specified range of the next line.

    Args:
        line (list[str]): The list of characters in the line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1
    return False


def checkPrevLine(line: list[str], lowerBound: int, upperBound: int) -> bool:
    """
    Checks if any special characters are present in the specified range of the previous line.

    Args:
        line (list[str]): The list of characters in the line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1
    return False


def checkLine(line: list[str], lowerBound: int, upperBound: int) -> bool:
    """
    Checks if any special characters are present in the specified range of the current line.

    Args:
        line (list[str]): The list of characters in the line to check.
        lowerBound (int): The starting index of the range to check.
        upperBound (int): The ending index (exclusive) of the range to check.

    Returns:
        bool: True if a special character (*, $, -, %, @, =, &, /, +, #) is found within the range, False otherwise.
    """
    while lowerBound < upperBound:
        if line[lowerBound] in ('*', '$', '-', '%', '@', '=', '&', '/', '+', '#'):
            return True
        lowerBound += 1
    return False


def read_in_without_whitespace(filepath):
    with open('day_5_input.txt') as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
    return lines