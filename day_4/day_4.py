import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities
import compare_lines

lines = utlities.readInInput('day_4_input.txt')

total_points = 0 

for line in lines:
    #initialize starting lists, and position(i = 2 to avoid Game #:)
    i = 2
    winning_numbers = []
    numbers_you_have = []

    while i < 12:
        #add all winning numbers from position 2 to 12 in the line into a list
        winning_numbers.append(line.split()[i]) 
        i += 1
    j = i
    while j < 38:
        #add all numbers that could be winners from position 13 to 38 in the line into a list
        numbers_you_have.append(line.split()[j]) 
        j += 1

    #compare the two lines, if there are no winning numbers no points are awarded
    if compare_lines.compare_lines(winning_numbers, numbers_you_have) == 0: 
        continue
    else:
        #compare the lines, return points and then calulate using 2^(points - 1)
        total_points += (2 ** (compare_lines.compare_lines(winning_numbers, numbers_you_have) - 1)) 
    
print(total_points)