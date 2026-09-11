def solution(progresses, speeds):
    answer = []
    days = []

    # 각 작업이 완료되는 데 필요한 날짜 계산
    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress

        day = remain // speed

        # 나누어 떨어지지 않으면 하루 더 필요
        if remain % speed != 0:
            day += 1

        days.append(day)

    # 첫 번째 작업을 기준으로 시작
    release_day = days[0]
    count = 1

    for i in range(1, len(days)):
        # 현재 작업이 앞 작업보다 빨리 끝나는 경우
        if days[i] <= release_day:
            count += 1

        # 현재 작업이 더 늦게 끝나는 경우
        else:
            answer.append(count)

            release_day = days[i]
            count = 1

    # 마지막 배포 묶음 추가
    answer.append(count)

    return answer
