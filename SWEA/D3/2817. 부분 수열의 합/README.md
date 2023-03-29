# [D3] 부분 수열의 합 - 2817 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB) 

### 성능 요약

메모리: 64,820 KB, 시간: 401 ms, 코드길이: 362 Bytes

### 풀이

- 앞서 풀이한 swea 1486번 장훈이의 높은 선반과 매우 유사한 문제이다.
- 조합으로 가능한 합을 구하고 그 합이 제시된 숫자 K와 동일하다면 카운팅하는 식으로 풀이했다.
- 앞선 문제와 다른 형식으로 풀이하고 싶어서 다르게 풀어봤다.
- start라는 임의의 수를 이용하여 이미 선택한 것은 제외하고 답을 구하는 식이다.
- 마지막까지 계산할 필요없이 K와 같은 값이라면 cnt+1, 큰값이라면 리턴했다.

> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
