import math


def readfile(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print ("Error opening or reading input file: ", filename)
        sys.exit()


def count_frequency_for_file(filename):
    """
    1. 모든 문자열을 소문자로 변경 - O(n)
    2. 문자열을 공백단위로 토크나이징 - O(n)
    3. 토큰 단위로 단어의 빈도수 카운팅 - O(n)
    O(n) = O(n) + O(n) + O(n)
    """
    frequency_vec = {}
    text = readfile(filename).lower()# O(n)
    for word in text.split():# split : O(n), loop : O(n)
        if word in frequency_vec:
            frequency_vec[word] = frequency_vec[word] + 1
        else:
            frequency_vec[word] = 1
    return frequency_vec


def inner_product(vec1, vec2):
    sum = 0
    for word in vec1:# O(n)
        if word in vec2:
            sum += vec1[word] * vec2[word]
    return sum


def vector_distance(vec1, vec2):
    numerator = inner_product(vec1, vec2)
    denominator = math.sqrt(inner_product(vec1,vec1)*inner_product(vec2,vec2))
    return math.acos(numerator/denominator)


def main():
    """
    두 문서간의 거리는 정규화된 두 문서벡터가 이루는 각의 크기로 한다.
    문자열이 일치해야만 유사도가 올라간다는 한계가 있다.
    """
    frequency_vector_1 = count_frequency_for_file("bobsey")
    frequency_vector_2 = count_frequency_for_file("lewis")
    distance = vector_distance(frequency_vector_1, frequency_vector_2)
    print ("The distance between the documents is: %0.6f (radians)"%distance)


if __name__ == "__main__":
    main()
