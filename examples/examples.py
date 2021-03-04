"""Exemplify how this package can be used."""

import time

from src.input import create_chain_from_file
from src.output import create_sentence

FILE_1 = 'genesis-en.txt'
FILE_2 = 'manchetes_bbb_21.txt'
LENGTH = 10


def example_1():
    for i in range(0, 10):
        create_sentence(create_chain_from_file(FILE_1), LENGTH)


def example_2():
    for name in ['Karol', 'Fiuk', 'Lumena', 'Viih', 'Projota', 'Nego']:
        create_sentence(create_chain_from_file(FILE_2), LENGTH, name)


start_time = time.perf_counter()
example_1()
print("--- %s seconds ---" % (time.perf_counter() - start_time))
