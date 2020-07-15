import random
from operator import attrgetter


def select_random(individuals, k):
    return [random.choice(individuals) for i in range(k)]


def select_best(individuals, k, fit_attr="fitness"):
    return sorted(individuals, key=attrgetter(fit_attr), reverse=True)[:k]


def select_worst(individuals, k, fit_attr="fitness"):
    return sorted(individuals, key=attrgetter(fit_attr))[:k]


def select_tournament(individuals, k, tournsize, fit_attr='fitness'):
    chosen = []
    for _ in range(k):
        aspirants = select_random(individuals, tournsize)
        chosen.append(max(aspirants, key=attrgetter(fit_attr)))
    return chosen


def select_roulette(individuals, k, fit_attr='fitness'):
    # descending order
    s_inds = sorted(individuals, key=attrgetter(fit_attr), reverse=True)
    sum_fits = sum(getattr(ind, fit_attr) for ind in individuals)
    chosen = []
    for _ in range(k):
        u = random.random() * sum_fits
        sum_ = 0
        for ind in s_inds:
            sum_ += getattr(ind, fit_attr)
            if sum_ > u:
                chosen.append(ind)
                break
    return chosen
