# 최대값이 k인 0이상의 정수배열 array를 정렬
def counting_sort(array, k):
    count, output = [0]*(k+1), [0]*len(array)
    for key in array:
        count[key] = count[key] + 1
    for i in range(k):
        count[i+1] = count[i+1] + count[i]
    for key in array:
        output[count[key]-1] = key
        count[key] = count[key] - 1
    return output


def counting_sort2(array, k):
    L = [[] for nothing in range(k+1)]
    for key in array:
        L[key].append(key)
    output = []
    for i in range(k+1):
        output.extend(L[i])
    return output


def main():
    print(counting_sort([1, 2, 3, 4], 4))
    print(counting_sort([4, 3, 2, 1, 5, 6, 4], 6))
    print(counting_sort2([1, 2, 3, 4], 4))
    print(counting_sort2([4, 3, 2, 1, 5, 6, 4], 6))


if __name__ == "__main__":
    main()
