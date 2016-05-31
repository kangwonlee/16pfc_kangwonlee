# coding: utf-8


def factorial(n):
    if 1 == n:
        result = 1
    elif 1 < n:
        result = n * factorial(n - 1)
    else:
        die('factorial : n smaller than 1')
    return result


def die(why):
    print('dead: %s' % why)
    from sys import exit
    exit(-1)


if __name__ == '__main__':
    f = factorial(5)
    print(f)
