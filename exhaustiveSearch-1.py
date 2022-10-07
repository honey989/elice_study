# LV2. 완전탐색 - 소수 찾기
from itertools import permutations
# 소수 판별 함수
def checkPrime(n):
    if n < 2:                                 
        return False
            
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True
                   
def solution(numbers):
    answer = []
    # 문자열 자르기
    numbers = list(numbers)
    temp = []
    # 자른 문자열로 순열 만들기
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i))
    # 만든 순열 숫자로 변환
    num = [int(''.join(t)) for t in temp] 
    # 소수 판별 후 정답 리스트에 넣기
    for i in num:
        if checkPrime(i):
            answer.append(i)
    # set으로 중복 제거후 길이 반환
    return len(set(answer))




