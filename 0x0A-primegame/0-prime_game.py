#!/usr/bin/python3
""" prime_game module """


def count_prime_nums(n):
    """ count number of prime numbers
    """
    primes = [True for _ in range(n + 1)]

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    output = [i for i in range(2, n + 1) if primes[i]]
    return len(output)


def isWinner(x, nums):
    """ determine who the winner of each game is """
    wins = []

    for i in range(x):
        n = nums[i]
        count = count_prime_nums(n)
        if count % 2 == 0:
            wins.append("Ben")
        else:
            wins.append("Maria")

    maria_wins_number = wins.count("Maria")
    ben_wins_number = wins.count("Ben")

    if maria_wins_number > ben_wins_number:
        return "Maria"
    elif ben_wins_number > maria_wins_number:
        return "Ben"
    else:
        return None
