import sys
sys.path.append('/Users/garrettkolenbrander/Code/2023_advent_of_code/')
import utlities
import split_list
import check_map

lines = utlities.readInInput('day_5_input.txt')


seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

maps = [seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

map_index = 0
for line in lines:
    line = line.strip()
    if line:
        maps[map_index].append(line)
    else:
        map_index += 1

seeds = lines[0].split()
maps[0] = seeds



for i in range( 8):
    maps[i] = split_list.split_list(maps[i])



seed_index = 0
seed_input = maps[0][seed_index]
for l in range (1,7):
    print(seed_input)
    seed_input = check_map.check_initial_range(seed_input, maps[l])

