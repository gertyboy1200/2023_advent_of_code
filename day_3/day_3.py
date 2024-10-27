# step 4: check the surounding places for special characters
# step 5: if it is a valid part number add to total sum

import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities

# step 1: read in file 
lines = utlities.readInInput('day_3_input.txt')

# step 2: assign each line of file to a list
for line in lines:
    newIndex = 0
    for i in range(len(line)):
# step 3: find the int ranges in each line ie. if there is a 3 digit number its range may be line[2]-line[5]
        #print(newIndex)
        if newIndex > len(line)- 2:
            break
        if line[newIndex].isdigit():
           #print(line[i])
           newIndex = utlities.checkNextNumber(line, i) 
        newIndex += 1
        #print(newIndex)

