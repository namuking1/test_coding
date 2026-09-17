#dfs x=x일때 1 x 다른거면 1 그리고 false로 배열을 설정해서 검증을 하는 작업으로 풀어봤습니다.


def solution(n, computers):
    answer = 0
    visi=[False]*n
    def dfs(x):
        visi[x]=True
        for i in range(0,n):
            if computers[x][i]==1 and not visi[i]:
                dfs(i)
    for i in range(0,n):
        if not visi[i]:
            dfs(i)
            answer += 1

    return answer
