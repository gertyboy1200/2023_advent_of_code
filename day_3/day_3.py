import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities

# step 1: read in file 
lines = utlities.readInInput('day_3_input.txt')
validInt = []
total = 0

# step 2: assign each line of file to a list
for lineIndex, line in enumerate(lines):
    i = 0
    while i < 140:
        
# step 3: find the int ranges in each line ie. if there is a 3 digit number its range may be line[2]-line[5]
        if line[i].isdigit():
            validInt =  utlities.checkNextNumber(line, i)
            sizeOfValidInt = utlities.nextNumberLength(validInt)
            i = utlities.checkNextNumberIndex(line, i)

# step 4: check the surounding places for special characters
# step 5: if it is a valid part number add to total sum
            if lineIndex + 1 < len(lines):
                if utlities.checkNextLine(lines[lineIndex + 1], (i - (sizeOfValidInt + 1)), i + 1):
                  total += validInt

            if lineIndex - 1 >= 0:
                if utlities.checkPrevLine(lines[lineIndex - 1], (i - (sizeOfValidInt + 1)), i + 1):
                    total += validInt

            if utlities.checkLine(lines[lineIndex], (i - (sizeOfValidInt + 1)), i + 1):
                total += validInt

        i += 1

print(total)



