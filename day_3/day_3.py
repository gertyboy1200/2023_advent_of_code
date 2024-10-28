# step 4: check the surounding places for special characters
# step 5: if it is a valid part number add to total sum

import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities

# step 1: read in file 
lines = utlities.readInInput('day_3_input copy.txt')
validInt = []
# step 2: assign each line of file to a list
for lineIndex, line in enumerate(lines):
    i = 0
    while i < 140:
# step 3: find the int ranges in each line ie. if there is a 3 digit number its range may be line[2]-line[5]
        if line[i].isdigit():
            validInt = int(''.join(map(str, utlities.checkNextNumber(line, i))))
            x = len(str(validInt))
            i = utlities.checkNextNumberLength(line, i)
            
            if lineIndex + 1 < len(lines):
                utlities.checkNextLine(lines[lineIndex + 1], (i - (x + 1), i)
            if lineIndex - 1 >= 0:
                print("oi")



             
        i += 1



