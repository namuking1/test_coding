
dfs 트리

def solution(numbers, target):
    answer = 0
    def df(index,total):
        nonlocal answer
        if index==  len(numbers):
            if total==target:
                answer+=1
            return
          #+1
        df(index+1,total+numbers[index])
          #-1 용도
        df(index+1,total-numbers[index])
    df(0,0)
    return answer
