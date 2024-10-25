with open('day_2_input.txt') as file:
    lines = file.readlines()

# Valid number of cubes: 12 red cubes, 13 green cubes, and 14 blue cubes
# Get game number for sum
def getGameNumber(gameLine):
    return int(''.join(filter(str.isdigit, gameLine[1])))


    
for line in lines:
    gameLine = line.split()
    gameNumber = getGameNumber(gameLine)
    print(" ")
    print(gameNumber)
    numOfCubesIndex = 2   # To skip output of "Game"
    colorIndex = 3
    for i in gameLine:
        if numOfCubesIndex % 2 == 0:
            print(gameLine[numOfCubesIndex])
        elif numOfCubesIndex > len(gameLine) - 2:
            break
        


        if colorIndex % 2 != 0:
            print(gameLine[colorIndex])
        elif colorIndex > len(gameLine) - 2:
            break

        if gameLine[colorIndex][-1] == ';':
            print("NEW SUB GAME. DICE DRAWN", gameLine[colorIndex])
        elif gameLine[colorIndex][-1] == ',':
            print("DICE DRAWN", gameLine[colorIndex])
        elif colorIndex == len(gameLine) - 1:
            print("DICE DRAWN", gameLine[colorIndex])

        numOfCubesIndex += 1
        colorIndex += 1






