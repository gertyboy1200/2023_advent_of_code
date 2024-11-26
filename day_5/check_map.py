def check_initial_range(seed, map_to_be_checked):
    #for line in map_to_be_checked:
        #print(line)
    seed = int(seed)
    for i in range(len(map_to_be_checked)):
        destination_range_lower_bound = map_to_be_checked[i][0]
        destination_range_upper_bound = int(destination_range_lower_bound) + int(map_to_be_checked[i][2])
        print("destination range: ", destination_range_lower_bound, " - ",destination_range_upper_bound )

        initial_range_lower_bound = map_to_be_checked[i][1]
        initial_range_upper_bound = int(initial_range_lower_bound) + int(map_to_be_checked[i][2])
        print("initial range: ", initial_range_lower_bound, " - ", initial_range_upper_bound)

        adjust_value = int(destination_range_lower_bound) - int(initial_range_lower_bound)

        if int(seed) > int(initial_range_lower_bound) and int(seed) < int(initial_range_upper_bound):
            print(seed)
            print("TRUE")
            return int(seed) + adjust_value

