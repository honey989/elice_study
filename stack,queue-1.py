# LV2. 스택/큐 - 올바른 괄호
def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 스택에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 올바르지 않은 괄호 짝이면 False 반환
                return False
            else:
                stack.pop()  # 올바른 괄호 짝이면 스택에서 '(' 제거
    
    return stack==[] 