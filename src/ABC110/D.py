from collections import defaultdict
import math


def run(n, m):
    MAX = 10**9+7
    count = search_divisor_num_2(m)
    return 2**count * n % MAX


def make_prime_list_2(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]


def prime_factorization_1(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list_2(num_sqrt)

        dict_counter = defaultdict(int)
        for prime in prime_list:
            while num % prime == 0:
                dict_counter[prime] += 1
                num //= prime
        if num != 1:
            dict_counter[num] += 1

        dict_counter = dict(dict_counter)

        return dict_counter


def search_divisor_num_2(num):
    if num < 0:
        return None
    elif num == 1:
        return 1
    else:
        divisor_num = 1
        dict_fact = prime_factorization_1(num)
        for value in dict_fact.values():
            divisor_num *= (value + 1)
        return divisor_num


def main():
    n, m = map(int, input().split())
    print(run(n, m))


if __name__ == '__main__':
    main()
