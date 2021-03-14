"""Exemplify how this package can be used."""

import time

from src.input import create_chain_from_file
from src.output import create_sentence

FILE = 'genesis-en.txt'
LENGTH = 10
SENSITIVITY = 0
AMOUNT = 10


def example():
    print(f'Generating {AMOUNT} new {LENGTH}-word sentences'
          f' with a sensitivity of {SENSITIVITY}/1 based on {FILE}:\n')

    for i in range(0, AMOUNT):
        print(f'{i + 1}. ' + create_sentence(create_chain_from_file(FILE),
                                             LENGTH, SENSITIVITY) + '\n')


if __name__ == '__main__':
    start_time = time.perf_counter()
    example()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
