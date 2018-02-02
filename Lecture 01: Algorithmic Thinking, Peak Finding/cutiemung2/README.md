# Peak Finding
<br />


## Peak이란?

다음과 같은 1차원 배열이 있다고 하자.

![1d_array](https://user-images.githubusercontent.com/35156601/35719571-5f80741e-082d-11e8-9da1-7594e98ab093.JPG)


그러면 Peak은 다음을 뜻한다.
 b>=a 이고 b>=c 이면 b는 peak이다.
양 끝에 존재하는 요소 i의 경우에는 
i>=h 이면 peak이다.

위의 Peak의 규칙에서 알 수 있듯이 하나의 배열안에는 두개 이상의 Peak이 존재 할 수 있다.

<br />

## 목표

배열이 주어졌을 때, 존재하는 하나의 Peak값을 찾아내는 것이다. 여러개라도 하나만 찾으면 된다.
최댓값을 찾는문제는 아니다. 그저 양 옆의 값이 자신보다 크지않다면 그 값을 Peak으로 선택하면 된다.
입력은 1차원과 2차원 배열로 주어진다.


## 1차원 배열에서의 Peak Finding

<br />

### 1. 직관적인 방법

비교적 쉽게 생각할 수 있는 알고리즘이다.
배열의 왼쪽에서 시작하여 비교를 통해 오른쪽으로 한칸씩 나아가는 방법이다.
최악의 경우 n번의 비교연산을 진행하게 되어 Θ(n)의 시간복잡도를 보인다.

본인이 작성한 코드는 다음과 같다.
```
//# python3.6
def straightforward_1D(self,input_numbers):
    length = len(input_numbers)
    for idx in range(length-1):
        if input_numbers[idx]>=input_numbers[idx+1]:
            return input_numbers[idx]
        
    return input_numbers[length-1]
```

<br />

### 2. 좀 더 효율적인 방법 - Divide and Conquer

더 빠른 알고리즘을 원한다면 조금은 더 복잡한 방법이 필요하다.

그 중 하나의 방법으로 이진 탐색을 사용 할 수 있는데, 배열을 반으로 쪼개가며 탐색 범위를 좁혀 나가기 때문에 "Divide and Conquer" 방식이라고 부른다. 

알고리즘은 다음과 같다.
· 먼저, 탐색 대상인 배열의 정 가운데를 선택한다.
· 선택된 값과 인접한 양 옆의 값을 비교한다.
· 왼쪽 값이 더 크다면 배열 정 중앙 기준으로 왼쪽에 있는 부분을 새로운 탐색대상으로 설정하여 반복한다.
· 그렇지 않고 오른쪽 값이 더 크다면 배열 정 중앙 기준으로 오른쪽에 있는 부분을 새로운 탐색대상으로 설정한다.
· 둘 다 아니라면, 즉 양옆에 자신보다 큰 값이 없다면 해당 값을 Peak으로 설정하고 탐색을 마친다.

본인이 작성한 코드는 다음과 같다.

```
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
```

이 알고리즘은 이전에 했던 직관적인 방법보다 속도면에서 효율이 뛰어나다. 
직관적인 방법은 한번 비교할 때마다 탐색대상이 1개씩 줄어들었는데, 이 경우에는 한번 비교할 때마다 탐색 대상이 반으로 줄어드니
데이터 양이 많을수록 빠른 속도를 보여준다.  Θ(log(n))의 시간복잡도를 가진다.

![1d](https://user-images.githubusercontent.com/35156601/35719949-03303ecc-082f-11e8-8ff7-577357434b2e.jpg)

<br />

## 2차원 배열에서의 Peak Finding

2차원에서는 1차원 규칙이 확장된다.
아래와 같은 2차원 배열이 존재할 때, a>= b, c, d, e이면 a는 Peak이다.

![2dpeak](https://user-images.githubusercontent.com/35156601/35719978-24cc8aa4-082f-11e8-8119-bf6dda2acfd3.JPG)

<br />

### 1. 직관적인 방법 (Greedy Ascent)
직관적인 방법으로는 첫번째 인덱스부터 마지막인덱스까지 하나하나 비교하는 방법이 있다.
또, 현재 상태에서 가장 큰 값을 쫒아가는 Greedy한 방법도 있을 수 있다.
이 외에도 생각할 수 있는 방법은 여러개가 있는데, 여기서는 그 중 하나를 사용할 것이다.


알고리즘 순서는 다음과 같다.
· 배열상에서 임의의 위치를 잡는다. 인접한 셀 4개 중에서 자신보다 큰 값이 발견되면 그 곳으로 위치를 옮긴다.
· 셀 4개중에 자신보다 큰 값이 없으면 그 값이 Peak이다.

배열의 크기가 n x m이라면 최악의 경우 n x m번의 비교과정을 거쳐야하므로 Θ(nm)의 시간복잡도를 보인다.

본인이 작성한 코드다.
```
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
```

<br />

### 2. 좀 더 효율적인 방법 - Divide and Conquer

2차원 배열에서 역시, 1차원과 비슷한 방식으로 연산횟수를 대폭 줄일 수 있다.
1차원에서 사용했던 Divide and Conquer 알고리즘을 살짝만 바꾸어 2차원에 적용시켜보겠다.

n개의 행(row)과 m개의 열(col)을 가지는 배열이 있다고 하자.

우선, 가운데에 있는 열을 선택한다. m/2번째 열이 되겠다.

![fake1](https://user-images.githubusercontent.com/35156601/35720112-b3b69f3e-082f-11e8-8a5f-a1a4e27cc366.JPG)
<br />

해당 m/2번째 열을 하나의 1차원 배열로 보고 그 안에서 Peak을 찾는다.
1차원 Peak Finding을 그대로 적용하면 될 것이다.

![fake2](https://user-images.githubusercontent.com/35156601/35720125-c3e345a6-082f-11e8-8df4-01494d9e03a5.JPG)

<br />
열에서 Peak이 찾아지면, 해당 값이 속해있는 행(row)을 선택하여 그 안에서 또 다시 1차원 Peak Finding을 진행한다.

![fake3](https://user-images.githubusercontent.com/35156601/35720131-c66d970e-082f-11e8-9b6f-81b2db8992e3.JPG)

행에서 얻어진 Peak을 최종적인 Peak으로 설정한다.

언뜻보면 그럴싸하게 보일 수도 있겠다. 하지만, 최종 선정된 위치의 위, 아래 값이 해당 Peak보다 크지 않을 거라는 보장이 없다.

위 방법의 단점을 보완하여 조금만 바꿔보면 괜찮은 알고리즘을 얻을 수 있다.

- - - - - - - -

![real3](https://user-images.githubusercontent.com/35156601/35720164-e251a834-082f-11e8-9c55-31910e35ca43.JPG)

먼저, 기존 방식대로 열의 정 중앙을 잡는다.
열을 하나의 1차원 배열로 생각하고 가장 큰 값을 찾는다. Peak을 찾는것이아니라 최댓값을 찾는다.

<br />

![real1](https://user-images.githubusercontent.com/35156601/35720165-e28d8534-082f-11e8-96fe-9d8fe2f4ad63.JPG)

최댓값과 양옆을 비교하여 더 큰 값이 있다면 해당 방향으로 탐색 열을 이동시킨다.

<br />

![real2](https://user-images.githubusercontent.com/35156601/35720167-e2bc215a-082f-11e8-8601-8a49ae8395e4.JPG)

이동 된 열에서 또 다시 최댓값을 찾고 양옆과 비교하는 작업을 반복한다. (사실 한쪽만 비교해도 상관없다)
양 옆의 값이 모두 자신보다 크지 않을 경우 Peak으로 선택한다.

본인이 구현한 코드이다.

```
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
```

위 과정을 따르면 처음에 소개했던 잘못된 알고리즘의 허점을 커버할 수 있다.
Θ(nlogm)의 시간복잡도를 보인다.
(아래 풀이에서 log(n)이 아니라 log(m)이 맞다, 그리고 맨 아래의 표는 신경쓰지 않아도 된다.)

![2d](https://user-images.githubusercontent.com/35156601/35720200-039ff838-0830-11e8-904b-c8e38fd2f5e3.jpg)

<br />

그런데, 왜 특정 열에서 하나의 값을 선택 할 때, Peak이 아닌 최댓값을 찾아야 할까? 
아래의 경우와 같이 운이 좋지 않으면 무한루프에 빠지게된다.

![whymax](https://user-images.githubusercontent.com/35156601/35720223-12c50eb6-0830-11e8-8b23-ac0d512535b6.JPG)

**빨간색은 각각의 열에서 1차원 Peak을 선정하여 탐색한 결과이고
파란색은 각각의 열에서 최댓값을 선정하여 탐색한 결과이다.**

열에서 Peak을 선정할 경우 최종 Peak을 찾지 못하고 무한루프에 빠지게 된다.
그렇기 때문에 현재 열의 최댓값을 선택함으로써, 다음 열을 처리 할 때 이전 열의 값이 더 커서 되돌아오는 상황을 방지 할 수 있다.
