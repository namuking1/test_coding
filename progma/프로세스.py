from collections import deque

def solution(priorities, location):
    queue = deque()

    # (원래 위치, 우선순위) 형태로 큐에 넣기
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    count = 0

    while queue:
        current = queue.popleft()

        # 현재 프로세스보다 우선순위가 높은 게 큐에 있는지 확인
        if any(current[1] < process[1] for process in queue):
            queue.append(current)
        else:
            # 실행
            count += 1

            # 실행한 프로세스가 우리가 찾던 프로세스라면 종료
            if current[0] == location:
                return count
