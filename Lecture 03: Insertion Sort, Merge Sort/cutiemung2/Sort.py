#import numpy as np # 테스트케이스 출력을 위해서만 사용

class Sort:
    def __init__(self):
        pass
    
    def insertion_sort(self, list):
        length = len(list)
        for key_idx in range(1,length):
            for idx in reversed(range(key_idx)):
                if list[idx] > list[idx+1]:
                    tmp = list[idx]
                    list[idx]=list[idx+1]
                    list[idx+1]=tmp
                else:
                    break
        return list
    
    def binary_insertion_sort(self, list):
        length = len(list)
        for key_idx in range(1,length):
            myhome = key_idx
            key = list[key_idx]
            first,last = 0, key_idx-1
            #binary search
            while first < last:
                mid = (first+last)//2
                if list[mid]<key:
                    first = mid+1
                else:
                    last = mid-1
                    
            if list[first]>key:
                myhome = first
            else:
                myhome = first+1
            
            for idx in reversed(range(myhome,key_idx)):
                list[idx+1] = list[idx]
            list[myhome] = key
        return list

    def merge_sort(self, list):
        length = len(list)
        if length<=1:
            return list
        
        front, rear = list[:length//2], list[length//2:]
        front_len, rear_len = len(front), len(rear)
        
        self.merge_sort(front)
        self.merge_sort(rear)
        
        front_idx, rear_idx = 0, 0
        del list[:]
        while front_idx<front_len and rear_idx<rear_len:
            if front[front_idx] < rear[rear_idx]:
                list.append(front[front_idx])
                front_idx+=1
            else:
                list.append(rear[rear_idx])
                rear_idx+=1
                
        if front_idx<front_len:
            list += front[front_idx:]
        else:
            list += rear[rear_idx:]
        
        return list
'''    
def print_array(array):
    print(np.array(array))
'''

def main():
    s = Sort()
    testcase = [[7,1,5,3,8,2,9],
                [1],
                [-1,2,0],
                [0,1,0,2,6,4,5,0,1,4,3],
                [9,8,7,6,5,4,3,2,1,0],
                [1,1,1]
               ]
    for tc in testcase:
        print("insertion_sort")
        print(s.insertion_sort(tc))
        print("binary_insertion_sort")
        print(s.binary_insertion_sort(tc))
        print("merge_sort")
        print(s.merge_sort(tc))
        print("- - - - - - - -\n")

if __name__ == "__main__":
    main()