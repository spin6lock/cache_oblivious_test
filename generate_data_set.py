# encoding: utf8
from config import set_size, test_set_size, sort_data_filename, \
    test_data_filename, set_rand_range, test_data_rand_range

import random
random.seed()


def generate(set_size, set_rand_range, out_filename):
    data = []
    for i in range(1, set_size):
        data.append(random.randint(*set_rand_range))
    data = sorted(data)
    data.insert(0, str(set_size))
    with open(out_filename, "w") as fout:
        content = '\n'.join([str(d) for d in data])
        fout.write(content)


if __name__ == "__main__":
    generate(set_size, set_rand_range, sort_data_filename)
    generate(test_set_size, test_data_rand_range, test_data_filename)
