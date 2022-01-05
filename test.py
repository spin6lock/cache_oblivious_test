from main import construct_bfs, breadth_first_search

from config import set_size, test_set_size, sort_data_filename, \
    test_data_filename, set_rand_range, test_data_rand_range

vals = [83, 123, 181, 190, 220]
struct = construct_bfs(vals)
print("struct:", struct)
print(breadth_first_search(struct, 0))
