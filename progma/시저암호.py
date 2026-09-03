
#ord()와 chr()를 이용해 시저 암호를 구현했습니다.
python3이용했구요

문자열을 한 글자씩 확인하면서 다음과 같이 처리했습니다.

공백인 경우에는 그대로 answer에 추가했습니다.
대문자인 경우 'A' <= c <= 'Z' 조건으로 판별했습니다.
소문자는 대문자와 공백을 제외한 나머지 문자로 처리했습니다.
ord()를 이용해 문자를 숫자로 변환한 뒤 n만큼 이동시켰습니다.
알파벳은 총 26개이기 때문에 % 26을 사용하여 Z를 넘어가면 다시 A부터 시작하도록 했습니다.
마지막으로 chr()를 이용해 숫자를 다시 문자로 변환했습니다.
#
def solution(s, n):
    answer = ''
    for c in s:
        if c ==' ':
            answer+=' '
        elif 'A'<=c<='Z':
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))

        else:
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return answer
