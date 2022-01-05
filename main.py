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


def construct_preorder_struct(sort_data):
    result = []
    recursive_build(result, sort_data)
    return result


def get_child(direction, item, sort_data):
    if item[direction][0] > item[direction][1]:
        return
    child_index = (item[direction][0] + item[direction][1]) // 2
    left = (item[direction][0], child_index-1)
    right = (child_index + 1, item[direction][1])
    val = sort_data[child_index]
    return {
            "val": val,
            "left": left,
            "right": right,
        }


def construct_bfs(sort_data):
    result = []
    open_list = []
    middle_index = len(sort_data) // 2
    middle_val = sort_data[middle_index]
    open_list.append({
        "val": middle_val,
        "left": (0, middle_index - 1),
        "right": (middle_index + 1, len(sort_data) - 1),
        })
    while len(open_list) != 0:
        item = open_list.pop(0)
        if item == -1:
            result.append(item)
            continue
        else:
            result.append(item["val"])
        left_child = get_child("left", item, sort_data)
        right_child = get_child("right", item, sort_data)
        if left_child == right_child and right_child is None:
            continue
        if left_child:
            open_list.append(left_child)
        else:
            open_list.append(-1)
        if right_child:
            open_list.append(right_child)
        else:
            open_list.append(-1)
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


def pre_order_binary_search(arr, val):
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
            result[index] = r
        else:
            result[index] = i
    return result


def preorder_search(struct, rand_data):
    result = [0]*len(rand_data)
    for index, r in enumerate(rand_data):
        i = pre_order_binary_search(struct, r)
        if i >= 0:
            result[index] = r
        else:
            result[index] = i
    return result


def breadth_first_search(struct, r):
    middle_index = 0
    max_index = len(struct) - 1
    while True:
        left = 2 * middle_index + 1
        right = 2 * middle_index + 2
        middle_val = struct[middle_index]
        if middle_val == r:
            return middle_index
        if left > max_index:
            return -1
        if r < middle_val:
            middle_index = left
        else:
            middle_index = right


def cache_oblivious_search(struct, rand_data):
    result = [0]*len(rand_data)
    for index, r in enumerate(rand_data):
        i = breadth_first_search(struct, r)
        if i >= 0:
            result[index] = r
        else:
            result[index] = i
    return result


def main():
    global rand_data, struct1, struct2, struct3
    # read in random number
    rand_data = readin(test_data_filename)
    # read in sorted number
    sort_data = readin(sort_data_filename)
    struct1 = construct_sort_arr(sort_data)
    struct2 = construct_preorder_struct(sort_data)
    struct3 = construct_bfs(sort_data)
    # search in data structure, time it
    #print(normal_search(struct1, rand_data))
    #print(preorder_search(struct2, rand_data))
    print("normal:", timeit.timeit('normal_search(struct1, rand_data)', globals=globals(), number=timeit_count))
    print("preorder:", timeit.timeit('preorder_search(struct2, rand_data)', globals=globals(), number=timeit_count))
    print("level order(BFS):", timeit.timeit('cache_oblivious_search(struct3, rand_data)', globals=globals(), number=timeit_count))


if __name__ == "__main__":
    main()
