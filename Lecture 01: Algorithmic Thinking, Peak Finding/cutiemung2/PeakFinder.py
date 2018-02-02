import numpy as np # 테스트케이스 출력을 위해서만 사용

class PeakFinder:
    def __init__(self):
        pass
    
    def straightforward_1D(self,input_numbers):
        length = len(input_numbers)
        for idx in range(length-1):
            if input_numbers[idx]>=input_numbers[idx+1]:
                return input_numbers[idx]
            
        return input_numbers[length-1]
    
    def straightforward_2D(self,input_numbers):
        n, m = len(input_numbers), len(input_numbers[0]) # n,m = #row, #col
        row, col = n//2, m//2
        
        for _ in range(m*n):
            if row>0 and input_numbers[row-1][col] > input_numbers[row][col]:
                row = row-1
            elif row<n-1 and input_numbers[row+1][col] > input_numbers[row][col]:
                row = row+1
            elif col>0 and input_numbers[row][col-1] > input_numbers[row][col]:
                col = col-1
            elif col<m-1 and input_numbers[row][col+1] > input_numbers[row][col]:
                col = col+1
            else:    
                return input_numbers[row][col]
        print("logic error!")
        
    def div_and_conq_1D(self, input_numbers):
        length = len(input_numbers)
        first, last = 0, length-1 # first, last = 탐색대상의 처음과 마지막 인덱스
        
        while True:#first != last:
            mid = (first + last)//2
            if mid>first and input_numbers[mid-1] > input_numbers[mid]: #mid>0
                last = mid-1
            elif mid<last and input_numbers[mid+1] > input_numbers[mid]: #mid<length-1
                first = mid+1
            else:
                return input_numbers[mid]
        return input_numbers[first]
        
    def div_and_conq_2D(self, input_numbers):
        n, m = len(input_numbers), len(input_numbers[0]) # n,m = #row, #col
        col = m//2
        while True:
            # 해당 열에서 최댓값 찾기
            max_row = 0
            for row in range(1,n):
                if input_numbers[max_row][col] < input_numbers[row][col]:
                    max_row = row
            
            # 최대 row에서 양 옆과 비교하기
            if col>0 and input_numbers[max_row][col-1] > input_numbers[max_row][col]:
                col -= 1
            elif col<m-1 and input_numbers[max_row][col+1] > input_numbers[max_row][col]:
                col += 1
            else:
                return input_numbers[max_row][col]
        print("logic error!")

def print_array(array):
    print(np.array(array))

def main():
    finder = PeakFinder()
    testcase_1D = [ [3,7,1,3,16,2,7],
                   [1,1,1,1],
                   [2,5,3,9,11],
                   [7,3,8],
                   [-1,3],
                   [3] ]
    
    testcase_2D = [
        [ [1, 2, 3, 4],[ 5, 6, 7, 8],[ 9,10,11,12],[13,14,15,16] ],
        [ [16, 15, 14, 13],[12, 11, 10,  9],[ 8,  7,  6,  5],[ 4,  3,  2,  1] ],
        [[1,3,5,4],[2,4,6,5],[3,2,4,1],[3,4,2,1]],
        [[1,3,1,0,-1,-2,-3],[11,10,3,1,0,-1,-2],[2,8,6,2,1,0,-1],[6,5,4,3,2,1,0],[7,4,2,2,1,0,9],[8,11,3,5,6,3,2],[5,8,4,1,8,-1,-2]]]
    
    print("= = = = = = = = = =\n >> 1D:")
    for testcase in testcase_1D:
        result1 = finder.straightforward_1D(testcase)
        result2 = finder.div_and_conq_1D(testcase)
        print_array(testcase)
        print('Peak (straightforward) : ',result1)
        print('Peak (divide & conquer) : ',result2)
        print()
    
    print("= = = = = = = = = =\n >> 2D:")
    for testcase in testcase_2D:
        result1 = finder.straightforward_2D(testcase)
        result2 = finder.div_and_conq_2D(testcase)
        print_array(testcase)
        print('Peak (straightforward) : ',result1)
        print('Peak (divide & conquer) : ',result2)
        print()

if __name__ == "__main__":
    main()