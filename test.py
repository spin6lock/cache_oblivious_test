from main import binary_search, cache_friendly_search, construct_cache_friendly_struct, cache_friendly_binary_search, readin

from config import set_size, test_set_size, sort_data_filename, \
    test_data_filename, set_rand_range, test_data_rand_range

vals = [83, 123, 181]
sort_data = readin(sort_data_filename)
struct = construct_cache_friendly_struct(sort_data)
for val in vals:
    print("cache:", struct, "val:", val)
    print(cache_friendly_binary_search(struct, val))
