import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities

lines = utlities.readInInput('day_2_input.txt')
# Valid number of cubes: 12 red cubes, 13 green cubes, and 14 blue cubes

validGames = []

for line in lines:
    gameLine = line.split()
    gameNumber = utlities.getGameNumber(gameLine)
    numOfCubesIndex = 2   # To skip output of "Game"
    colorIndex = 3

    for i in gameLine:
        
        if numOfCubesIndex > len(gameLine) - 2:
            break

        if gameLine[colorIndex][-1] == ';':
            if utlities.isValid(gameLine, colorIndex, numOfCubesIndex) == False:
                #print("break")
                break

        elif gameLine[colorIndex][-1] == ',':
            if utlities.isValid(gameLine, colorIndex, numOfCubesIndex) == False:
                break

        elif colorIndex == len(gameLine) - 1:
            if utlities.isValid(gameLine, colorIndex, numOfCubesIndex):
                validGames.append(gameNumber)
            else:
                break

        numOfCubesIndex += 1
        colorIndex += 1

print(sum(validGames))





