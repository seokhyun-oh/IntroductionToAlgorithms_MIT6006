import random

primes = [2, 3, 5, 7, 11]


def lower_bound(n, s, e):
    while (e-s) > 0:
        mid = (s+e) // 2
        if n <= primes[mid]:
            e = mid
        else:
            s = mid+1
    return primes[s]


def get_prime_exceed(n):
    largest = primes[-1]
    if n <= largest:
        return lower_bound(n, 0, len(primes))
    for next in range(largest+2, n*2, 2):
        is_prime = True
        for p in primes:
            # if not prime
            if next % p == 0:
                is_prime = False
                break
            if next <= (p*p):
                break
        if is_prime:
            primes.append(next)
            if next >= n:
                return next

    return primes[-1]


class Univ:

    def __init__(self, size=8):
        self.size = size
        self.__setup__()

    def __setup__(self):
        self.p = get_prime_exceed(self.size*2) # p는 universal size 이상의 소수
        self.a = random.randint(0, self.p-1)
        self.b = random.randint(0, self.p-1)
        self.m = get_prime_exceed(self.size)

    def __call__(self, key):
        return ((self.a*key + self.b) % self.p) % self.m

    def grow(self):
        self.size = self.size * 2
        self.__setup__()
        return self.m

    def shrink(self):
        self.size = self.size // 2
        self.__setup__()
        return self.m

    def get_size(self):
        return self.m


class PrimeHash:
    """
    소수를 해시값으로 갖기위한 레퍼클래스.
    Universal hashing function으로부터 받은 해시값보다 큰 소수를 반환한다.
    """

    def __init__(self, size=8):
        self.h = Univ(size)

    def __call__(self, key):
        return get_prime_exceed(self.h(key))

    def grow(self):
        self.h.grow()

    def shrink(self):
        self.h.shrink()


class OANode:
    """
    open addressing을 위한 플레그
    노드를 삭제할 경우 NONE이 아닌 DELETED상태가 된다
    (키가 중복되는 이후노드를 찾을 수 없기때문)
    노드 삽입시 NONE, DELETED상태인 슬롯에만 저장된다.
    """
    NONE = 0
    USED = 1
    DELETED = 2

    def __init__(self):
        self.state = self.NONE
        self.item = None

    def insert(self, item):
        self.state = self.USED
        self.item = item

    def delete(self):
        self.state = self.DELETED
        self.item = None

    def is_none(self):
        return self.state == self.NONE

    def is_used(self):
        return self.state == self.USED

    def __str__(self):
        if self.item is None:
            return 'None'
        return self.item

    def __eq__(self, other):
        return self.item == other


class OAHash:

    def __init__(self):
        self.h1 = Univ()
        self.h2 = PrimeHash()

        self.capacity = 8 # h2의 값과 서로소이기 때문에 2^n형태의 값을 갖는다.
        self.size = 0
        self.items = [OANode() for _ in range(self.capacity)] # chaining방식과 다르게 상태를 저장하는 객체로 초기화한다.

    def insert(self, item):
        if self.capacity < self.size * 1.7: # USED/(NONE + DELETED) 가 0.5~0.6일때 리사이징하는게 효율이 좋다고 한다.
            self.__grow()
        self.__insert(item)
        self.size = self.size + 1

    def __insert(self, item):
        # double hashing방식으로 h2의 해시값은 m과 서로소관계이다.
        # 이를 쉽게 만들고자 h2는 2 이상의 소수, m은 2^n형태로 표현한다.
        k1, k2 = self.h1(item.__hash__()), self.h2(item.__hash__())
        for i in range(self.capacity):
            key = (k1 + i*k2) % self.capacity
            if not self.items[key].is_used():
                self.items[key].insert(item)
                return

    def delete(self, item):
        if self.__delete(item):
            self.size = self.size - 1

    def __delete(self, item):
        k1, k2 = self.h1(item.__hash__()), self.h2(item.__hash__())
        for i in range(self.capacity):
            key = (k1 + i*k2) % self.capacity
            if item == self.items[key]:
                self.items[key].delete()
                return True
        return False

    def __grow(self):
        self.h1.grow()
        self.h2.grow()
        self.capacity = self.capacity * 2
        self.__copy_items()

    def __copy_items(self):
        old = self.items
        self.items = [OANode() for _ in range(self.capacity)]
        for ele in old:
            if ele:
                self.__insert(ele.item)
            del ele
        del old

    def show_table(self):
        print('*-'*15)
        for i in range(len(self.items)):
            print('*', '{0} - {1}'.format(i, self.items[i]))
        print('*-'*15)
        print()


def main():
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
    oahash = OAHash()
    for i in range(0, 4):
        oahash.insert(data[i])
    oahash.show_table()

    for i in range(4, 15):
        oahash.insert(data[i])
    oahash.show_table()

    for i in range(15):
        oahash.delete(data[i])
    oahash.show_table()

    for i in range(15, len(data)):
        oahash.insert(data[i])
    oahash.show_table()


if __name__ == '__main__':
    main()
