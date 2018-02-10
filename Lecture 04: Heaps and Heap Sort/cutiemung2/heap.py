# 배열의 시작 인덱스는 1
class MaxHeapSort:
    def __init__(self):
        pass

    #precondition : S는 이미 max heap.
    def __extract_max(self, S):
        if len(S)==1:
            return None

        max = S[1]

        # 삭제 대상인 root와 마지막 노드를 swap한다
        tmp = S[-1]
        S[-1] = S[1]
        S[1] = tmp

        # 마지막 노드를 삭제한다.
        del S[-1]

        # root노드를 대상으로 정렬시킨다.
        self.max_heapify(S,1)

        return max


    def heap_sort(self, S):
        sorted_S = [None] + S
        length = len(sorted_S)
        self.build_max_heap(sorted_S) # O(n)
        S = [self.__extract_max(sorted_S) for _ in range(length-1)] # extract_max( O(logn) ) 를 n번 수행 : O(nlogn)
        return S

    
    def build_max_heap(self, S):
        for idx in reversed(range(1,(len(S)-1)//2+1)): # O(n) : leaf노드를 제외한 모든노드에 대해서 max_heapify를 호출
            self.max_heapify(S, idx) # O(logn) : 
            # 하지만 build_max_heap의 시간복잡도는 O(n)
            # 층이 올라갈수록 처리할 depth가 커지지만 동시에 한 층의 노드수도 줄어들기 때문

    #precondition : idx노드 기준 left와 right의 subtree는 이미 max heap.
    def max_heapify(self, S, idx): # log(n)
        length = len(S)
        left_idx, right_idx = idx*2, idx*2+1
        new_idx = idx

        # 루트와 자식을 비교
        if left_idx<length and S[idx]<S[left_idx]:
            new_idx = left_idx
        if right_idx<length and S[new_idx]<S[right_idx]:
            new_idx = right_idx
        
        # 루트가 더 작으면 가장 큰 애랑 스왑하고 
        # 그로인해 잘 정렬되어있던 child 서브트리가 깨졌으므로
        # 해당 노드를 대상으로 max_heap을 재귀호출
        if new_idx != idx:
            tmp = S[new_idx]
            S[new_idx] = S[idx]
            S[idx] = tmp
            self.max_heapify(S, new_idx)

def main():
    s = MaxHeapSort()
    testcase =[ [0, 5,2,1,3,8,6],
                [0, 1,2,3,4,5,6],
                [0, 6,5,4,3,2,1],
                [0, 10,9,7,8,6,5,4],
                [0, 5,4,6,3,7,2,8,1,9],
               []]

    print(*[s.heap_sort(tc) for tc in testcase],sep='\n')    

if __name__ == "__main__":
    main()
