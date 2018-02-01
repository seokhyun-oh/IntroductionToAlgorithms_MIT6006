class PeakFinder:

    def __init__(self):
        pass

    def one_dimensional_straightforward_find(self, numbers):
        n = len(numbers)
        if n == 0:
            raise Exception("There is no input number")
        if n == 1:
            return numbers[0]

        # 첫 원소와 마지막 원소는 두번째, n-1번째 원소와 비교한다.
        if numbers[0] >= numbers[1]:
            return numbers[0]
        if numbers[-1] >= numbers[-2]:
            return numbers[-1]

        # 나머지 원소들은 왼쪽부터 순서대로 비교하여 양 옆보다 크거나 같으면 그 값을 반환한다.
        for i in range(1, n-1):
            if numbers[i] >= numbers[i-1] and numbers[i] >= numbers[i+1]:
                return numbers[i]

    def one_dimensional_divide_and_conquer_find(self, numbers):
        n = len(numbers)
        if n == 0:
            raise Exception("There is no input number")
        if n == 1:
            return numbers[0]

        half = n//2
        # 가운데 원소가 그 왼쪽의 원소보다 작을경우 [1,n/2-1]범위의 원소들만 확인
        if numbers[half-1] > numbers[half]:
            return self.one_dimensional_divide_and_conquer_find(numbers[0:half-1])
        # 가운데 원소가 그 오른쪽의 원소보다 작을경우 [n/2+1,n]범위의 원소들만 확인
        elif numbers[half+1] > numbers[half]:
            return self.one_dimensional_divide_and_conquer_find(numbers[half, n])
        # 그 외의 경우 n/2번째 원소가 peak
        else:
            return numbers[half]

    def two_dimensional_straightforward_find(self, matrix):
        Y = len(matrix)
        X = len(matrix[0])

        for y in range(Y):
            for x in range(X):
                if y > 0 and matrix[y-1][x] > matrix[y][x]:
                    continue
                elif y < Y-1 and matrix[y+1][x] > matrix[y][x]:
                    continue
                elif x > 0 and matrix[y][x-1] > matrix[y][x]:
                    continue
                elif x < X-1 and matrix[y][x+1] > matrix[y][x]:
                    continue
                else:
                    return matrix[y][x]

    def look_for_max_idx(self, col):
        maxIdx = 0
        for i in range(len(col)):
            if col[i] > col[maxIdx]:
                maxIdx = i
        return maxIdx

    def two_dimensional_divide_and_conquer_find(self, matrix):
        half = len(matrix)//2
        maxIdx = self.look_for_max_idx(matrix[half])

        # matrix가 단일컬럼일 경우 그 컬럼의 최대값을 반환한다.
        if len(matrix) == 1:
            return matrix[half][maxIdx]

        # 해당 컬럼의 최대값보다 큰 값이 존재할 경우 나머지 절반을 배제하고 peak를 찾는다.
        if matrix[half-1][maxIdx] > matrix[half][maxIdx]:
            return self.two_dimensional_divide_and_conquer_find(matrix[:half])
        if matrix[half+1][maxIdx] > matrix[half][maxIdx]:
            return self.two_dimensional_divide_and_conquer_find(matrix[half+1:])
        return matrix[half][maxIdx]

