def swap(L, a, b):
    temp = L[a]
    L[a] = L[b]
    L[b] = temp


def LEFT(i):
    return 2 * i + 1


def RIGHT(i):
    return 2 * i + 2


def max_heapify(L, idx, size):
    """
    Correct a single violation of the heap property in a subtree's root.
    just choose a maximum value among root, left-child and right-child
    and make it tree's root
    """
    left, right = LEFT(idx), RIGHT(idx)
    max_idx = idx
    if left < size and L[left] > L[max_idx]:
        max_idx = left
    if right < size and L[right] > L[max_idx]:
        max_idx = right

    if idx != max_idx:
        swap(L, idx, max_idx)
        max_heapify(L, max_idx, size)


def build_max_heap(L):
    """
    Elements in range [size/2, size) will be heapified automatically bacause they are leaves
    구간 [size/2, size)의 원소들은 리프노드이기 때문에 힙 모양으로 자동으로 정리됩니다.
    """
    size = len(L)
    for i in range(size//2-1, -1, -1):
        max_heapify(L, i, size)


def heap_sort(L):
    """
    step1 : build_max_heap from unordered array.
    step2 : find max element A[0]
    step3 : swap elements A[n] with A[0]
    step4 : discard node n from the heap(decrementing heap size)
    step5 : New root may violate max_heap but children are max_heap(max_heapify)
    repeat step2 to step5 until array is sorted
    """
    # step1 : 정렬되지않은 배열로부터 힙 자료구조형태로 만들어줌
    build_max_heap(L)
    for i in range(len(L)-1, 0, -1):
        # step2 : 최대값을 갖는 원소인 A[0]를 찾는다
        # step3 : 마지막 원소인 A[n]과 A[0]를 교환한다
        swap(L, 0, i)
        # step4 : heap size를 감소시키는 방법으로 A[n]을 제거한다
        # step5 : 루트가 max_heap을 만족하지않기때문에 다시 힙 구조로 만들어준다
        max_heapify(L, 0, i)
    return L


def main():
    testcases = [
        [1, 4, 3, 5, 6, 3, 4, 8],
        [5, 4, 6, 3, 2, 3, 6, 7],
        [9, 4, 3, 2, 6, 3, 7, 1],
        [3, 2, 1, 4, 5, 3, 2, 0],
        [8, 5, 4, 6, 3, 2, 9, 1]
    ]
    for tc in testcases:
        print(heap_sort(tc))


if __name__ == "__main__":
    main()

