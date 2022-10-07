# LV2. 힙 - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    # 스코빌 리스트 최소 힙으로 만들기
    heapq.heapify(scoville)
    # 스코빌 최솟값이 K보다 크거나 같아질 때까지
    while scoville[0] < K:
        # 가장 작은 값, 두번째로 작은 값 섞기
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        # 섞은 값 넣어주기
        heapq.heappush(scoville, mix)
        answer += 1
        # 다 섞어도 K보다 작은 경우
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
