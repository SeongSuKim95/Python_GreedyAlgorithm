import time
start_time = time.time_ns()*1000
#input N,M,K

# 5, 8, 3
# 2, 4, 5, 4 ,6

# 입력 받는 방법 : input()-> 한 줄의 문자열을 입력 받음
# 문자열을 int type으로 casting -> map(int, ~)
# 데이터 공백 구분 : input().split()
# 결과를 list로 casting : list()

# n, m, k = map(int, input().split())
# data = list(map(int,input().split()))

n, m, k = 5 ,8 ,3
data = [2,4,5,4,6]
# My answer

start_time =int(round(time.time()*1000))

###
data.sort() ## built in 정렬


First = data[n-1]
Second = data[n-2]

iter = m // (k+1)
Remainder = m % (k+1)
Sum = iter*(First*k+Second)+First*Remainder ## int (M/(K+1)) *K + M %(K+1)
print(Sum)
###
end_time =int(round(time.time()*1000))
print("time : ",end_time - start_time)

## P93
start_time =int(round(time.time()*1000))
Sum = 0

while True:
    for i in range(k):
        if m == 0 :
            break
        Sum += First
        m -= 1
    if m == 0 :
        break
    Sum += Second
    m -= 1

print(Sum)

end_time =int(round(time.time()*1000))
print("time : ",end_time - start_time)

## P95
n, m, k = 5 ,8 ,3
start_time =int(round(time.time()*1000))

count = int(m/(k+1))*k ## First count for iteration
count += m %(k+1) ## First count for Remainder

result = 0
result += count*First
result += (m-count)*Second

print(result)

end_time =int(round(time.time()*1000))
print("time : ",end_time - start_time)

