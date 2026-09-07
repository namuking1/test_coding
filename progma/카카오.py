#이 문제는 먼저 두 문자열을 전부 소문자로 바꿔서 대문자와 소문자의 차이를 없앴다. 그다음 각 문자열을 앞에서부터 두 글자씩 잘라서, 두 글자가 모두 영문자인 경우에만 리스트에 넣었다. 예를 들어 "FRANCE"는 "fr", "ra", "an", "nc", "ce"처럼 나눌 수 있다.

#이후 두 리스트를 비교하면서 같은 문자열이 있으면 교집합의 개수를 1씩 증가시켰다. 이때 같은 원소를 여러 번 잘못 세는 것을 막기 위해 두 번째 리스트를 복사한 뒤, 이미 교집합으로 사용한 원소는 복사한 리스트에서 삭제했다.

#합집합의 개수는 첫 번째 리스트의 개수와 두 번째 리스트의 개수를 더한 뒤, 두 번 포함된 교집합의 개수를 한 번 빼서 구했다.

#마지막으로 교집합 크기 / 합집합 크기로 자카드 유사도를 계산하고, 문제에서 요구한 대로 65536을 곱한 뒤 소수점 아래를 버렸다. 만약 두 리스트가 모두 비어 있다면 자카드 유사도를 1로 정의하므로 65536을 반환했다.

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    A = []
    B = []

    for i in range(len(str1) - 1):
        word = str1[i:i+2]

        if 'a' <= word[0] <= 'z' and 'a' <= word[1] <= 'z':
            A.append(word)

    for i in range(len(str2) - 1):
        word = str2[i:i+2]

        if 'a' <= word[0] <= 'z' and 'a' <= word[1] <= 'z':
            B.append(word)

  
    if len(A) == 0 and len(B) == 0:
        return 65536

   
    temp = B.copy()
    intersection = 0

    for word in A:
        if word in temp:
            intersection += 1
            temp.remove(word)

    union = len(A) + len(B) - intersection

    return int(intersection / union * 65536)
