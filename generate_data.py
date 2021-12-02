""" Generate a bunch of data to be analyzed later.
"""

from random import randrange

def generate_data(an_id, mini, maxi):
    while True:
        yield (an_id, randrange(mini, maxi))

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
