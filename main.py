#encoding:utf8

from config import set_size, test_set_size, sort_data_filename, \
    test_data_filename, set_rand_range, test_data_rand_range, timeit_count
import random
import timeit


def readin(filename):
    with open(filename) as fin:
        data = [int(d) for d in fin.readlines()]
        return data[1:]


def construct_sort_arr(sort_data):
    return sort_data


def recursive_build(result, remain):
    if len(remain) == 0:
        return
    middle_index = len(remain) // 2
    middle_val = remain[middle_index]
    result.append(middle_val)
    recursive_build(result, remain[0:middle_index])
    recursive_build(result, remain[middle_index + 1:])


def construct_cache_friendly_struct(sort_data):
    result = []
    recursive_build(result, sort_data)
    return result


def binary_search(arr, val):
    left = 0
    right = len(arr)
    max_index = right - 1
    while True:
        middle_index = (left + right) // 2
        if middle_index > max_index:
            return -1
        middle_val = arr[middle_index]
        if val == middle_val:
            return middle_index
        if val < middle_val:
            right = middle_index - 1
        else:
            left = middle_index + 1
        if left > right or right < 0 or left > max_index:
            return -1


def cache_friendly_binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    middle_index = left
    max_index = right
    while True:
        middle_val = arr[middle_index]
        if val == middle_val:
            return middle_index
        if val < middle_val:
            left = left + 1
            right = (left + right) // 2
        else:
            left = (left + right + 1) // 2 + 1
        middle_index = left
        if left > right:
            return -1


def normal_search(struct, rand_data):
    result = [0]*len(rand_data)
    for index, r in enumerate(rand_data):
        i = binary_search(struct, r)
        if i >= 0:
            result[index]= r
        else:
            result[index] = i
    return result    


def cache_friendly_search(struct, rand_data):
    result = [0]*len(rand_data)
    for index, r in enumerate(rand_data):
        i = cache_friendly_binary_search(struct, r)
        if i >= 0:
            result[index]= r
        else:
            result[index] = i
    return result    


def main():
    global rand_data, struct1, struct2
    # read in random number
    rand_data = readin(test_data_filename)
    # read in sorted number
    sort_data = readin(sort_data_filename)
    struct1 = construct_sort_arr(sort_data)
    struct2 = construct_cache_friendly_struct(sort_data)
    # search in data structure, time it
    #print(normal_search(struct1, rand_data))
    #print(cache_friendly_search(struct2, rand_data))
    print("normal:", timeit.timeit('normal_search(struct1, rand_data)', globals=globals(), number=timeit_count))
    print("cache friendly:", timeit.timeit('cache_friendly_search(struct2, rand_data)', globals=globals(), number=timeit_count))


if __name__ == "__main__":
    main()
