def sqrt(a, n=2):
    EPSILON = 0.5e-16
    x = a
    x_next = a+1
    operation = 0
    print('-'*70)
    while abs((x_next-x)/x) > EPSILON:
        x = x_next
        x_next = x - (x**n - a) / (n*(x**(n-1)))
        operation = operation + 1
        print('{0} operation : {1}'.format(operation, x))
    print('{0}-square root of {1} is {2}'.format(n, a, x))


def main():
    sqrt(624, 4)
    sqrt(625, 4)


if __name__ == '__main__':
    main()
