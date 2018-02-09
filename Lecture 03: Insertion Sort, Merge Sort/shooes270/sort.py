import random as r

def swap(L, a, b):
    temp = L[a]
    L[a] = L[b]
    L[b] = temp

def insertion_sort(L):
    size = len(L)
    key = 1
    while key < size:
        cursor = key
        while cursor > 0 and L[cursor-1] < L[cursor]:
            swap(L, cursor-1, cursor)
            cursor -= 1
        key += 1
    return L


def merge(left, right):
    L_sorted = []
    l, r = 0, 0
    l_size, r_size = len(left), len(right)
    while l < l_size and r < r_size:
       if left[l] >= right[r]:
           L_sorted.append(left[l])
           l += 1
       else:
           L_sorted.append(right[r])
           r += 1
    if l < l_size:
        L_sorted += left[l:]
    if r < r_size:
        L_sorted += right[r:]
    return L_sorted


def merge_sort(L, s, e):
    """
    [s,e)구간 병합정렬
    """
    if e-s < 2:
        return L[s:e]
    left = merge_sort(L, s, (e+s)//2)
    right = merge_sort(L, (e+s)//2, e)
    return merge(left, right)


def fast_merge_sort(L, s, e):
    """
    insertion sort의 효율이 높은 구간에서는 insertion sort를 사용하도록 변경
    정렬의 효율성에 대한 계산은 critical_point.py에 구현되어있다.
    """
    if e-s < 66:
        return insertion_sort(L)
    left = fast_merge_sort(L, s, (e+s)//2)
    right = fast_merge_sort(L, (e+s)//2, e)
    return merge(left, right)


def main():
    L = 1000*[None]
    for i in range(1000):
        L[i] = r.random()
    fast_merge_sort(L[:], 0, len(L))
    merge_sort(L[:], 0, len(L))
    insertion_sort(L[:])


if __name__ == "__main__":
    import profile
    profile.run("main()")

