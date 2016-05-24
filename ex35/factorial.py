# coding: utf-8


def factorial(n):
    if 1 == n:
        result = 1
    elif 1 < n:
        result = n * factorial(n - 1)
    return result


if __name__ == '__main__':
    f = factorial(5)
    print(f)
