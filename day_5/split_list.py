def split_list(seed_map):
    seed_map_2 = []
    del seed_map[0]
    for test in seed_map:
        test = test.split()
        seed_map_2.append(test)
    seed_map = seed_map_2
    return seed_map