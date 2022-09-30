# LV2. 해시 - 전화번호 목록
def solution(phone_book):
    answer = True
    hash_map = {}
    # 딕셔너리에 저장
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # 딕셔너리에 해당 값이 있는지 확인
    # 같은 번호는 제외
    for phone_number in phone_book:
        tmp = ""
        for i in phone_number:
            tmp += i
            if tmp in hash_map and tmp != phone_number:
                answer = False
    return answer