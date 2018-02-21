import math
import random


class String:

    def __init__(self, text=''):
        self.text = text
        self.hashcode = None

    def __hash__(self):
        if self.hashcode is None:
            self.hashcode = self.__hashcode__()
        return self.hashcode

    def __str__(self):
        return self.text

    def __hashcode__(self):
        """
        pre-hash function
        hashcode = s[0]*(31^(n-1)) + s[1]*(31^(n-2)) ... s[n-1])
        """
        hashcode = 0
        digit = math.pow(31, len(self.text)-1)
        for c in self.text:
            hashcode = hashcode + int(ord(c)*digit)
            digit = digit // 31
        return hashcode


def div():
    """
    Division 방식은 렌덤값 m으로 키값을 나눈 나머지를 이용한다.
    이때 m은 2와 10의 지수승에 가깝지않은 소수여야한다.
    """
    m = 73

    def calc(key):
        return key % m
    return calc


def mul():
    r = 6 # 최대 2^6개의 키값을 저장
    w = 32 # 64비트 환경에선 64를 사용
    m = int(math.pow(2, w))
    a = random.randint(m//2, m) # a는 홀수이며 구간 (2^(w-1), 2^w)에서 랜덤하게 선택.
    if a%2 == 0:
        if a-m//2 > m-a: # a가 2^w에 더 가까울 경우
            a = a-1
        else:
            a = a+1

    def calc(key):
        k = key % m # 오버플로우 방지 (타 언어 참고용)
        return (a*k % m) >> (w-r)
    return calc


def univ(size=100):
    def get_prime_exceed(s):
        if s < 3:
            return 2
        is_prime = [True] * (s*2 + 1) # 소수정리에 의해 구간 [s, 2s]에 적어도 한개의 소수가 존재
        is_prime[0] = is_prime[1] = False
        for i in range(len(is_prime)):
            if is_prime[i]:
                if i > s:
                    return i
                for step in range(i*2, len(is_prime), i):
                    is_prime[step] = False
        return -1

    p = get_prime_exceed(size) # p는 universal size 이상의 소수
    a = random.randint(0, p-1)
    b = random.randint(0, p-1)
    m = 73 # division방식과 같은 방법으로 구함, 단 p보다 작아야함

    def calc(key):
        k = key % m
        return ((a*k + b) % p) % m
    return calc


class Hash:

    def __init__(self, hash_function=div()):
        self.h = hash_function
        self.items = [None for _ in range(100)]

    def insert(self, item):
        key = self.h(item.__hash__())
        if self.items[key] is None:
            self.items[key] = [item]
        else:
            self.items[key].append(item)

    def browse(self):
        L = []
        for key in range(len(self.items)):
            if self.items[key] is not None:
                L.append("{0} : {1}".format(key, self.items[key]))
        return L


def main():
    hash_functions = [div(), mul(), univ()]
    data = [
        'exercitation', 'incididunt', 'Lorem', 'culpa',
        'Ut', 'enim', 'veniam', 'consectetur', 'occaecat',
        'magna', 'dolore', 'do', 'minim', 'ex',
        'ipsum', 'nulla', 'qui', 'sit', 'deserunt',
        'mollit', 'ea', 'cillum', 'voluptate', 'sint',
        'dolor', 'nostrud', 'velit', 'id', 'nisi',
        'laboris', 'irure', 'est', 'labore', 'Duis',
        'proident', 'sunt', 'aliquip', 'in', 'reprehenderit',
        'eiusmod', 'Excepteur', 'ullamco', 'fugiat', 'aliqua',
        'quis', 'anim', 'amet', 'et', 'sed',
        'pariatur', 'consequat', 'esse', 'cupidatat', 'commodo',
        'eu', 'adipiscing', 'officia', 'tempor', 'elit',
        'ad', 'non', 'ut', 'aute', 'laborum'
    ]
    for f in hash_functions:
        hash = Hash(hash_function=f)
        for word in data:
            hash.insert(word)
        for line in hash.browse():
            print(line)
        print('-------------------------')


if __name__ == "__main__":
    main()
