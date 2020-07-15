import random
from itertools import repeat
from collections.abc import Sequence


def mutate_gaussian(individual, mu, sigma, indpb):
    size = len(individual)
    if not isinstance(mu, Sequence):
        mu = repeat(mu, size)
    elif len(mu) < size:
        raise IndexError(
            f"mu must be at least the size of individual: {len(mu)} < {size}")

    if not isinstance(sigma, Sequence):
        sigma = repeat(sigma, size)
    elif len(sigma) < size:
        raise IndexError(
            f"sigma must be at least the size of individual: {len(sigma)} < {size}")

    for i, m, s in zip(range(size), mu, sigma):
        if random.random() < indpb:
            individual[i] += random.gauss(m, s)

    return individual,


def mutate_shuffle_indexes(individual, indpb):
    size = len(individual)
    for i in range(size):
        if random.random() < indpb:
            swap_indx = random.randint(0, size - 2)
            if swap_indx >= i:
                swap_indx += 1
            individual[i], individual[swap_indx] = \
                individual[swap_indx], individual[i]

    return individual,


def mutate_flip_bit(individual, indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] = type(individual[i])(not individual[i])

    return individual,
