#1이 될때까지

#N, K = map(int, input().split())
N = 25
K = 3
cnt = 0
loop = 0
## MY answer
while True:
    loop+=1
    if N == 1:
        break
    else :
        if N % K == 0:
            N //= K
        else :
            N -=1

        cnt +=1

print(cnt, loop)

##
N = 25
K = 3
result = 0
loop =0
while True:
    loop+=1
    # N==K 로 나누어 떨어질때 까지 1씩 뺀다
    target = (N//K)*K
    result += (N - target)
    N = target
    # N이 K보다 작을때 탈출
    if N < K:
        break
    result += 1
    N //= K

#마지막으로 남은 수에 대해 1씩 뺀다
result += (N-1)
print(result,loop)

## 두 code의 차이점 : 코드는 위가 더 간단하지만 while loop의 수가 더 많다.