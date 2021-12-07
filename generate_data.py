""" Generate a bunch of data to be analyzed later.
"""

from random import randrange

def generate_data(an_id, dow, mini, maxi):
    while True:
        yield (randrange(mini, maxi), dow, an_id)

def get_generated():
    c = 100
    generator1a = generate_data(1, 1, 840, 855)
    generator1b = generate_data(1, 2, 825, 900)
    generator2 = generate_data(2, 1, 885, 960)
    data = []
    while c:
        c -= 1
        data.append(next(generator1a))
        data.append(next(generator1b))
        data.append(next(generator2))
    return data

if __name__ == '__main__':
    c = 1000
    generator1a = generate_data(1, 840, 855)
    generator1b = generate_data(1, 825, 900)
    generator2 = generate_data(2, 885, 960)
    while c:
        c -= 1
        print(next(generator1a))
        print(next(generator1b))
        print(next(generator2))
