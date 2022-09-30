# LV2. 스택/큐 - 기능개발
def solution(progresses, speeds):
    answer = []
    
    while progresses: # 프로그레스 빌때까지
        for i in range(len(progresses)):
            progresses[i] += speeds[i] # 작업의 진도를 증가
        cnt = 0
        # 작업이 남아있고 맨 앞 작업 진도가 100인 경우
        # 배포 개수 증가, 해당 작업과 작업 속도 제거
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0: # 배포할 기능이 있다면 추가
            answer.append(cnt)
            
    return answer