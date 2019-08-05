# 1
# delta 사용
'''
ary[0...n-1][0...n-1]
dx[] = [0, 0, -1, 1] #상 하 좌 우
dy[] = [-1, 1, 0, 0]

for x in range (len(ary)):
    for y in range(len(ary[x])):
        for i in range(4):
            testX <- x + dx[mode]
            testY <- y + dy[mode]
            test(ary[testX][testY])


# 전치행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
'''

# 2
# 비트사용해서 부분합 찾기
# 어떤 수 i에서 j번째 bit는 뭘까? == i의 j번째 비트가 1인지 아닌지를 리턴함.
'''
if (i&(1<<j))

ex)
6 & (1<<2)
0 1 1 0 & 0 1 0 0 = 0 1 0 0 --> 0 1 0 0 나옴 --> 3 번째 원소를 부분집합에 넣어라.
'''

# 부분집합 생성하는 방법
cnt = 0
arr = [1, 2, 3, 4, 5, 6]   # n=6 이니까 2^6개만큼의 부분집합이 만들어질 수 있다.

n = len(arr)

for i in range(1<<n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교  /  n, n+1 결과값은 같지만 n+1일 때는 항상 0이라서 할 필요 없음
        if i & (1<<j):  # i의 j번째 비트가 1이면, j번째 원소 출력
            print(arr[j], end=", ")
    cnt += 1
    print()
print()
print(cnt)


# 3
# 검색
'''
(1) 순차검색 : O(n)  (정렬 / 비정렬)
비정렬된 경우
'''
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        if i < n:
            return i
        else:
            return -1

# 정렬된 경우

def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
        if i < n and a[i] == key:
            return i
        else:
            return -1
'''
(2) 이진검색 : O(n)
데이터가 정렬되었다고 가정하고 탐색
중간 숫자를 찾아서 찾는 수와 비교한 후, 작은부분, 큰부분을 나눠서 또 사이 수와 비교
'''

def binarySearch(a, key):
    start <= 0
    end <= len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1  # end를 middle앞 번호로 바꾼다.
        else:
            start = middle + 1  # start를 middle 뒤번호로 바꾼다.
    return False  # 검색 결과 없음

'''
(3) 선택 알고리즘 : O(n^2)
한 step 안에서, 

가장 왼쪽에 있는 값이 가장 작은 값이라고 가정한 뒤, 
그 오른쪽에 있는 요소들 중에 더 작은 값이 있으면 그 곳의 index를 저장해 놓는다
(계속 update한다).
이런 식으로 끝까지 도달했을 때의 index값을 기준으로, 
가장 왼쪽에 있는 값과 swap하면 정말로 가장 작은 값이 놓이게 된다.
출처: https://starkying.tistory.com/entry/Bubble-Sort-버블-정렬-Selection-Sort-선택-정렬 [Random Access Memories]

근데 버블소트와 다른점은?
버블소트는 맨 앞에서부터 두 값씩 비교해서 정렬하는 것.
선택 알고리즘은 맨 앞을 가장 작은값으로 보고 맨 앞 vs 나머지 리스트의 값들을 비교하면서 정렬
'''

# 큰 숫자를 오른쪽으로 이동하는 선택정렬 코드
public class Main {
    public static void main(String[] args) {
        int[] intArray = { 20, 35, -15, 7, 55, 1, -22 };
        // 각 pass가 끝날 때마다 lastUnsortedIndex 위치에 가장 큰 값이 위치해야 한다.
        for (int lastUnsortedIndex = intArray.length - 1; lastUnsortedIndex > 0;
                lastUnsortedIndex--) {
            int largest = 0;    // 가장 큰 값이 위치한 index
            // largest를 0으로 놓고 i는 1부터 시작
            for (int i = 1; i <= lastUnsortedIndex; i++) {
                if (intArray[i] > intArray[largest]) {
                    largest = i;
                }
            }
            // intArray[largest]와 intArray[lastUnsortedIndex] 교환
            swap(intArray, largest, lastUnsortedIndex);
        }
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }
    }
    public static void swap(int[] array, int i, int j) {
        if (i == j) {
            return;
        }
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
# 출처: https://starkying.tistory.com/entry/Bubble-Sort-버블-정렬-Selection-Sort-선택-정렬 [Random Access Memories]

# k번째로 작은 원소를 찾는 알고리즘

def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
