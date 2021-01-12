import timeit

## 숫자 card game
N,M = map(int,input().split())
## My answer

## M 크기를 가진 리스트 생성 ( 0, 1, 2, ... M)

min_list = list(range(M))

for i in range(N):
  list_A = list(map(int,input().split()))
  min_value = min(list_A)
  ## 변수명과 built_in function이 같지 않게 하자
  min_list[i] = min_value

print(max(min_list))

##
result = 0
for i in range(N):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value) ## list에 저장하지 않고 그때 그때 비교

print(result)