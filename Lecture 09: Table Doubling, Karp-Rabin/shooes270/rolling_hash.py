import math


class String:

    def __init__(self, str):
        self.str = [c for c in str]
        self.hash = None
        self.base = 256 # 문자열의 최대값보다 커야 해시충둘이 일어날 가능성이 적다.
        self.bases = {x: int(math.pow(self.base, x)) for x in range(len(str)+1)}
        self.__hash__()

    def __hash__(self):
        if self.hash is not None:
            return self.hash
        self.hash = 0
        for c in self.str:
            self.hash = self.base*self.hash + ord(c)
        return self.hash

    def append(self, c):
        self.str.append(c)
        self.hash = self.base*self.hash + ord(c)

    def skip(self):
        c = self.str.pop(0)
        self.hash = self.hash - ord(c)*self.bases[len(self.str)]

    def __eq__(self, other):
        return self.str == other.str


def contains(s, t):
    L = len(s)

    if s == t[:L]:
        return True

    rs = String(s)
    rt = String(t[0:L])

    for i in range(L, len(t)):
        rt.skip()
        rt.append(t[i])
        if rs.hash == rt.hash and rs == rt:
            return True
    return False


def main():
    s = 'test'
    t = 'This is testcase'
    print(contains(s, t))

    t = 'This is case'
    print(contains(s, t))


if __name__ == '__main__':
    main()
