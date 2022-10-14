def solution(people, limit):
    answer = 0
    # 오름차순 정렬
    people.sort()
    # 포인터 두개 설정
    start, end = 0, len(people) - 1
    while start <= end:
        answer += 1
        # 두 포인터 합이 제한 무게를 넘지 않으면 한번에 태워보냄
        if people[start] + people[end] <= limit:
            start += 1
        # 그렇지 않으면 한사람만 태워보냄
        end -= 1
    
    return answer
