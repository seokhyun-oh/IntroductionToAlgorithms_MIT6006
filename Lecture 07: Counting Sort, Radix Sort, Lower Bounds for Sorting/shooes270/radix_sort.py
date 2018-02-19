def counting_sort_for_radix(array, k, callback):
    L = [[] for nothing in range(k+1)]
    for ele in array:
        key = callback(ele)
        L[key].append(ele)
    output = []
    for i in range(k+1):
        output.extend(L[i])
    return output


# 1의 자리수부터 순서를 유지하며 정렬
def radix_sort(array):
    m = max(array)
    digit = 1
    while m//digit > 0:
        array = counting_sort_for_radix(array, 9, lambda x: x//digit % 10)
        digit = digit*10
    return array


def main():
    testcases = [
        [123, 423, 552, 1536, 1123],
        [423, 164, 928, 1103, 12342],
        [12345, 553, 999, 1293, 9999],
        [9853, 8871, 1132, 0, 12]
    ]
    for tc in testcases:
        print(radix_sort(tc))


if __name__ == "__main__":
    main()
