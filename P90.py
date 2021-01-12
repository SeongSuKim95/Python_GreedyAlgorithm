
#### 동전을 거슬러주는 문제

n = 1260
count = 0

coin_types = [500,100,50,10] # coin types

for coin in coin_types:
    count +=  n // coin  #
    n %= coin

print(count)

## Key point
## Greedy 알고리즘은 최적의 해를 찾을 수 없을 가능성이 높다.
## 100,50,10이 500의 약수이기 때문에 가능했던 것.

