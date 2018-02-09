"""
파이썬으로 merge sort를 실행할 경우 2.2nlgn의 시간이 걸리고
insertion sort를 실행할 경우 0.2n^2의 시간이 걸린다
이 때 insertion sort를 사용하는게 더 효율적인 최대 입력의 개수를 구하는 코드이다.
"""
import math


def is_more_efficient(n):
    return 11*math.log2(n) >= n


def main():
    n = 2
    while is_more_efficient(n):
        n *= 2
    while not is_more_efficient(n):
        n -= 1
    print(n)


if __name__ == "__main__":
    main()
