import math

def formation(number, base):
    result = ""
    while number:
        result = str(number % base) + result
        number = number // base
    return result

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(num ** 0.5)
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    formation_result = [int(num) for num in formation(n, k).split('0') if num]
    for num in formation_result:
        if is_prime(num):
            answer += 1
    return answer