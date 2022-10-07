# LV2. 정렬 - 가장 큰 수
def solution(numbers):
    # 리스트 int형에서 string으로
    numbers = list(map(str, numbers))
    # key 조건에 맞게 정렬(numbers 1000이하이므로 문자열 3번 반복)/내림차순 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 모든 값이 0일때를 처리하기 위해 int -> str 변환
    return str(int(''.join(numbers)))
