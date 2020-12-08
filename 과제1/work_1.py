from collections import deque
# 1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다.
# L 또는 R은 대소문자 모두 입력 가능하다.
Word,Integer,Direction=map(str,input().split())
Rotate_Loop=int(Integer)
Rotate_Word=deque(Word)

# 2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
if Direction=='L' or Direction=='l':
   Rotate_Word.rotate(-Rotate_Loop)
elif Direction=='R' or Direction=='r':
     Rotate_Word.rotate(Rotate_Loop)

print("".join(Rotate_Word))
