import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities

    
lines = utlities.read_in_without_whitespace('day_5_input.txt')

#for line in lines:
    #print(line.split())
seeds = [0]
seed_to_soil = [1]
soil_to_fertilizer = [2]
fertilizer_to_water = [3]
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

maps = [seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

#for line in lines:
    #print(line)

#print(lines[0])

#for line in lines:
    #test = line.split()[0]
    #if test.isdigit:
        #print(line.split()[0])
        #print("AHHHHHH")
index = 1
map_index = 1
def get_map(lines, index):

    temp_list = []

    for line in lines:
        txt = line.split()[0]

        if txt.isdigit() == False:
            #print(txt)
            #print(lines[index - 1])
            #print(lines[index])
            for i in range(index + 1, 164):
                #print(i)
                check = lines[i]
                check2 = check.split()
                if check2[0].isdigit():
                    temp_list.append(check2)
                else:

                    return temp_list

        index += 1

    return temp_list

def get_index(lines, index):

    temp_list = []

    for line in lines:
        txt = line.split()[0]

        if txt.isdigit() == False:
            #print(txt)
            #print(lines[index - 1])
            #print(lines[index])
            for i in range(index + 1, len(lines) - 1):
                #print(i)
                check = lines[i]
                check2 = check.split()
                if check2[0].isdigit():
                    temp_list.append(check2)
                    #print(temp_list)
                else:

                    return i

        index += 1

    return i

index = 1
for j in range(7):
    print(index)
    maps[map_index] = get_map(lines, index)
    map_index += 1
    index = get_index(lines, index)
    print(maps[j])













