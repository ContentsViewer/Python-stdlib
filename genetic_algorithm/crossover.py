import random
import copy


def cross_one_point(ind1, ind2):
    size = min(len(ind1), len(ind2))
    xpoint = random.randint(1, size - 1)
    ind1[xpoint:], ind2[xpoint:] = ind2[xpoint:], ind1[xpoint:]

    return ind1, ind2


def cross_two_point(ind1, ind2):
    size = min(len(ind1), len(ind2))
    xpoint1 = random.randint(1, size)
    xpoint2 = random.randint(1, size - 1)

    if xpoint2 >= xpoint1:
        xpoint2 += 1
    else:
        # swap the two x points
        xpoint1, xpoint2 = xpoint2, xpoint1

    ind1[xpoint1:xpoint2], ind2[xpoint1:xpoint2] \
        = ind2[xpoint1:xpoint2], ind1[xpoint1:xpoint2]
    # print(xpoint1, xpoint2)
    return ind1, ind2


def cross_uniform(ind1, ind2, indpb):
    size = min(len(ind1), len(ind2))
    for i in range(size):
        if random.random() < indpb:
            ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2


def cross_partially_matched(ind1, ind2):
    size = min(len(ind1), len(ind2))
    p1, p2 = {}, {}
    # p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i

    # Choose crossover points
    xpoint1 = random.randint(0, size)
    xpoint2 = random.randint(0, size - 1)

    if xpoint2 >= xpoint1:
        xpoint2 += 1
    else:
        # Swap the two cross points
        xpoint1, xpoint2 = xpoint2, xpoint1

    for i in range(xpoint1, xpoint2):
        # Keep track of the selected values
        temp1 = ind1[i]
        temp2 = ind2[i]

        # Swap the matched value
        ind1[i], ind1[p1[temp2]] = temp2, temp1
        ind2[i], ind2[p2[temp1]] = temp1, temp2

        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2


# def cross_partially_matched(ind1, ind2):
#     size = min(len(ind1), len(ind2))
#     p1, p2 = {}, {}
#     # p1, p2 = [0] * size, [0] * size

#     # Initialize the position of each indices in the individuals
#     for i in range(size):
#         p1[ind1[i]] = i
#         p2[ind2[i]] = i

#     # Choose crossover points
#     xpoint1 = random.randint(0, size)
#     xpoint2 = random.randint(0, size - 1)

#     if xpoint2 >= xpoint1:
#         xpoint2 += 1
#     else:
#         # Swap the two cross points
#         xpoint1, xpoint2 = xpoint2, xpoint1

#     print(xpoint1, xpoint2)

#     ind1_org, ind2_org = copy.deepcopy(ind1), copy.deepcopy(ind2)

#     # Apply crossover between x points
#     for i in range(xpoint1, xpoint2):
#         # Keep track of the selected values
#         temp1 = ind1_org[i]
#         temp2 = ind2_org[i]

#         ind1[i], ind2[i] = temp2, temp1
#         if p1[temp2] < xpoint1 or xpoint2 <= p1[temp2]:
#             ind1[p1[temp2]] = temp1
#             p1[temp1], p1[temp2] = p1[temp2], p1[temp1]

#         if p2[temp1] < xpoint1 or xpoint2 <= p2[temp1]:
#             ind2[p2[temp1]] = temp2
#             p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

#     return ind1, ind2


def cross_uniform_partially_matched(ind1, ind2, indpb):
    size = min(len(ind1), len(ind2))
    p1, p2 = {}, {}

    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i

    for i in range(size):
        if random.random() < indpb:
            # Keep track of the selected values
            temp1 = ind1[i]
            temp2 = ind2[i]

            # Swap the matched value
            ind1[i], ind1[p1[temp2]] = temp2, temp1
            ind2[i], ind2[p2[temp1]] = temp1, temp2

            # Position bookkeeping
            p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
            p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2


def cross_ordered(ind1, ind2):
    size = min(len(ind1), len(ind2))
    a, b = random.sample(range(size), 2)
    if a > b:
        a, b = b, a

    # holes1, holes2 = [True] * size, [True] * size
    holes1, holes2 = set(), set()

    for i in range(size):
        if i < a or b < i:
            holes1.add(ind2[i])
            holes2.add(ind1[i])

    # We must keep the original values somowhere before scrambling everything
    temp1, temp2 = copy.deepcopy(ind1), copy.deepcopy(ind2)
    k1, k2 = b + 1, b + 1
    for i in range(size):
        if temp1[(i + b + 1) % size] in holes1:
            ind1[k1 % size] = temp1[(i + b + 1) % size]
            k1 += 1

        if temp2[(i + b + 1) % size] in holes2:
            ind2[k2 % size] = temp2[(i + b + 1) % size]
            k2 += 1
    # print(a, b)
    # Swap the content between a and b (included)
    for i in range(a, b + 1):
        ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2
