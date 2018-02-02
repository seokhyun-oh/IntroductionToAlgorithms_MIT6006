# Peak Finding
<br />


## Peak�̶�?

������ ���� 1���� �迭�� �ִٰ� ����.

![1d_array](https://user-images.githubusercontent.com/35156601/35719571-5f80741e-082d-11e8-9da1-7594e98ab093.JPG)


�׷��� Peak�� ������ ���Ѵ�.
 b>=a �̰� b>=c �̸� b�� peak�̴�.
�� ���� �����ϴ� ��� i�� ��쿡�� 
i>=h �̸� peak�̴�.

���� Peak�� ��Ģ���� �� �� �ֵ��� �ϳ��� �迭�ȿ��� �ΰ� �̻��� Peak�� ���� �� �� �ִ�.

<br />

## ��ǥ

�迭�� �־����� ��, �����ϴ� �ϳ��� Peak���� ã�Ƴ��� ���̴�. �������� �ϳ��� ã���� �ȴ�.
�ִ��� ã�¹����� �ƴϴ�. ���� �� ���� ���� �ڽź��� ũ���ʴٸ� �� ���� Peak���� �����ϸ� �ȴ�.
�Է��� 1������ 2���� �迭�� �־�����.


## 1���� �迭������ Peak Finding

<br />

### 1. �������� ���

���� ���� ������ �� �ִ� �˰����̴�.
�迭�� ���ʿ��� �����Ͽ� �񱳸� ���� ���������� ��ĭ�� ���ư��� ����̴�.
�־��� ��� n���� �񱳿����� �����ϰ� �Ǿ� ��(n)�� �ð����⵵�� ���δ�.

������ �ۼ��� �ڵ�� ������ ����.
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

### 2. �� �� ȿ������ ��� - Divide and Conquer

�� ���� �˰����� ���Ѵٸ� ������ �� ������ ����� �ʿ��ϴ�.

�� �� �ϳ��� ������� ���� Ž���� ��� �� �� �ִµ�, �迭�� ������ �ɰ����� Ž�� ������ ���� ������ ������ "Divide and Conquer" ����̶�� �θ���. 

�˰����� ������ ����.
�� ����, Ž�� ����� �迭�� �� ����� �����Ѵ�.
�� ���õ� ���� ������ �� ���� ���� ���Ѵ�.
�� ���� ���� �� ũ�ٸ� �迭 �� �߾� �������� ���ʿ� �ִ� �κ��� ���ο� Ž��������� �����Ͽ� �ݺ��Ѵ�.
�� �׷��� �ʰ� ������ ���� �� ũ�ٸ� �迭 �� �߾� �������� �����ʿ� �ִ� �κ��� ���ο� Ž��������� �����Ѵ�.
�� �� �� �ƴ϶��, �� �翷�� �ڽź��� ū ���� ���ٸ� �ش� ���� Peak���� �����ϰ� Ž���� ��ģ��.

������ �ۼ��� �ڵ�� ������ ����.

```
def div_and_conq_1D(self, input_numbers):
    length = len(input_numbers)
    first, last = 0, length-1 # first, last = Ž������� ó���� ������ �ε���
      
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

�� �˰����� ������ �ߴ� �������� ������� �ӵ��鿡�� ȿ���� �پ��. 
�������� ����� �ѹ� ���� ������ Ž������� 1���� �پ����µ�, �� ��쿡�� �ѹ� ���� ������ Ž�� ����� ������ �پ���
������ ���� �������� ���� �ӵ��� �����ش�.  ��(log(n))�� �ð����⵵�� ������.

![1d](https://user-images.githubusercontent.com/35156601/35719949-03303ecc-082f-11e8-8ff7-577357434b2e.jpg)

<br />

## 2���� �迭������ Peak Finding

2���������� 1���� ��Ģ�� Ȯ��ȴ�.
�Ʒ��� ���� 2���� �迭�� ������ ��, a>= b, c, d, e�̸� a�� Peak�̴�.

![2dpeak](https://user-images.githubusercontent.com/35156601/35719978-24cc8aa4-082f-11e8-8119-bf6dda2acfd3.JPG)

<br />

### 1. �������� ��� (Greedy Ascent)
�������� ������δ� ù��° �ε������� �������ε������� �ϳ��ϳ� ���ϴ� ����� �ִ�.
��, ���� ���¿��� ���� ū ���� �i�ư��� Greedy�� ����� ���� �� �ִ�.
�� �ܿ��� ������ �� �ִ� ����� �������� �ִµ�, ���⼭�� �� �� �ϳ��� ����� ���̴�.


�˰��� ������ ������ ����.
�� �迭�󿡼� ������ ��ġ�� ��´�. ������ �� 4�� �߿��� �ڽź��� ū ���� �߰ߵǸ� �� ������ ��ġ�� �ű��.
�� �� 4���߿� �ڽź��� ū ���� ������ �� ���� Peak�̴�.

�迭�� ũ�Ⱑ n x m�̶�� �־��� ��� n x m���� �񱳰����� ���ľ��ϹǷ� ��(nm)�� �ð����⵵�� ���δ�.

������ �ۼ��� �ڵ��.
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

### 2. �� �� ȿ������ ��� - Divide and Conquer

2���� �迭���� ����, 1������ ����� ������� ����Ƚ���� ���� ���� �� �ִ�.
1�������� ����ߴ� Divide and Conquer �˰����� ��¦�� �ٲپ� 2������ ������Ѻ��ڴ�.

n���� ��(row)�� m���� ��(col)�� ������ �迭�� �ִٰ� ����.

�켱, ����� �ִ� ���� �����Ѵ�. m/2��° ���� �ǰڴ�.

![fake1](https://user-images.githubusercontent.com/35156601/35720112-b3b69f3e-082f-11e8-8a5f-a1a4e27cc366.JPG)
<br />

�ش� m/2��° ���� �ϳ��� 1���� �迭�� ���� �� �ȿ��� Peak�� ã�´�.
1���� Peak Finding�� �״�� �����ϸ� �� ���̴�.

![fake2](https://user-images.githubusercontent.com/35156601/35720125-c3e345a6-082f-11e8-8df4-01494d9e03a5.JPG)

<br />
������ Peak�� ã������, �ش� ���� �����ִ� ��(row)�� �����Ͽ� �� �ȿ��� �� �ٽ� 1���� Peak Finding�� �����Ѵ�.

![fake3](https://user-images.githubusercontent.com/35156601/35720131-c66d970e-082f-11e8-9b6f-81b2db8992e3.JPG)

�࿡�� ����� Peak�� �������� Peak���� �����Ѵ�.

��溸�� �׷����ϰ� ���� ���� �ְڴ�. ������, ���� ������ ��ġ�� ��, �Ʒ� ���� �ش� Peak���� ũ�� ���� �Ŷ�� ������ ����.

�� ����� ������ �����Ͽ� ���ݸ� �ٲ㺸�� ������ �˰����� ���� �� �ִ�.

- - - - - - - -

![real3](https://user-images.githubusercontent.com/35156601/35720164-e251a834-082f-11e8-9c55-31910e35ca43.JPG)

����, ���� ��Ĵ�� ���� �� �߾��� ��´�.
���� �ϳ��� 1���� �迭�� �����ϰ� ���� ū ���� ã�´�. Peak�� ã�°��̾ƴ϶� �ִ��� ã�´�.

<br />

![real1](https://user-images.githubusercontent.com/35156601/35720165-e28d8534-082f-11e8-96fe-9d8fe2f4ad63.JPG)

�ִ񰪰� �翷�� ���Ͽ� �� ū ���� �ִٸ� �ش� �������� Ž�� ���� �̵���Ų��.

<br />

![real2](https://user-images.githubusercontent.com/35156601/35720167-e2bc215a-082f-11e8-8601-8a49ae8395e4.JPG)

�̵� �� ������ �� �ٽ� �ִ��� ã�� �翷�� ���ϴ� �۾��� �ݺ��Ѵ�. (��� ���ʸ� ���ص� �������)
�� ���� ���� ��� �ڽź��� ũ�� ���� ��� Peak���� �����Ѵ�.

������ ������ �ڵ��̴�.

```
def div_and_conq_2D(self, input_numbers):
    n, m = len(input_numbers), len(input_numbers[0]) # n,m = #row, #col
    col = m//2
    while True:
        # �ش� ������ �ִ� ã��
        max_row = 0
        for row in range(1,n):
            if input_numbers[max_row][col] < input_numbers[row][col]:
                max_row = row
          
        # �ִ� row���� �� ���� ���ϱ�
        if col>0 and input_numbers[max_row][col-1] > input_numbers[max_row][col]:
            col -= 1
        elif col<m-1 and input_numbers[max_row][col+1] > input_numbers[max_row][col]:
            col += 1
        else:
            return input_numbers[max_row][col]
    print("logic error!")
```

�� ������ ������ ó���� �Ұ��ߴ� �߸��� �˰����� ������ Ŀ���� �� �ִ�.
��(nlogm)�� �ð����⵵�� ���δ�.
(�Ʒ� Ǯ�̿��� log(n)�� �ƴ϶� log(m)�� �´�, �׸��� �� �Ʒ��� ǥ�� �Ű澲�� �ʾƵ� �ȴ�.)

![2d](https://user-images.githubusercontent.com/35156601/35720200-039ff838-0830-11e8-904b-c8e38fd2f5e3.jpg)

<br />

�׷���, �� Ư�� ������ �ϳ��� ���� ���� �� ��, Peak�� �ƴ� �ִ��� ã�ƾ� �ұ�? 
�Ʒ��� ���� ���� ���� ���� ������ ���ѷ����� �����Եȴ�.

![whymax](https://user-images.githubusercontent.com/35156601/35720223-12c50eb6-0830-11e8-8b23-ac0d512535b6.JPG)

**�������� ������ ������ 1���� Peak�� �����Ͽ� Ž���� ����̰�
�Ķ����� ������ ������ �ִ��� �����Ͽ� Ž���� ����̴�.**

������ Peak�� ������ ��� ���� Peak�� ã�� ���ϰ� ���ѷ����� ������ �ȴ�.
�׷��� ������ ���� ���� �ִ��� ���������ν�, ���� ���� ó�� �� �� ���� ���� ���� �� Ŀ�� �ǵ��ƿ��� ��Ȳ�� ���� �� �� �ִ�.
