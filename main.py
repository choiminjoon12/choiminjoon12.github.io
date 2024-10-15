# 정보처리기사 의미가 있습니다. <- 대학교 졸업생이 딴다.
# - 실제로 개발자로 일을 하는 사람이죠
# - 필요한건 오직 실력뿐 (만든 결과물 프로젝트, 코딩알고리즘 문제)
# - 웹개발 JS + Python 

 # random 모듈
# https://docs.python.org/ko/3/library/random.html


#cargoship
import random
random.seed(66) # 무작위 랜덤 기준을 변경
cargolist = [10, 35, 1, 2, 31, 5, 18, 19, 20, 21, 22, 4, 23, 15, 16, 17, 34, 7, 8, 30, 3, 24, 9, 36, 37, 38, 39, 14, 27, 28, 29, 25, 26, 6, 11, 12, 13, 33, 32]
random.shuffle(cargolist) # 리스트를 무잒위로 섞는걸 의미합니다.
# print(cargolist)


# 지난시간에 만든 스택블래스 있나요? 붙여넣기
class Stack:
  def __init__(self, e):
      self.stick = e
  def push(self,e):
      self.stick.append(e)
  def pcheck(self):
      if len(self.stick) <= 0:
          return True
      else:
          return False

  def pop(self):
      if self.pcheck() == False:
          ee =self.stick[-1]
          # 리스트에어 값을 제거하는 방법 del 원하는 값
          del self.stick[-1]
          return ee
      else:
          print('비어있는 스택')

  def printc(self):
      print(self.stick)


# le 빈리스트 대신에 쓰는 스택
# staack의 push 어디서해야할까?

# staack = Stack([])

# 클래승
print("cargo======")
# 큰화물선 cargo
cargo = Stack(cargolist)
cargo.printc()


# 작은 화물선 - Stack 클래스로 만들어보기
carback = Stack([])

# 화물 운송시스템 시뮬레이션
# 5개씩 작은 화물선으로 옮겨갑니다. -> 함수
# 맨 위에서부터 5개씻 뽑아소 옮기기
# 16번째 화물이 어디에 있는지

# 입력값 e: 큰화물선 / a : 작은화물선
def left(e,a):
  # 5개씩 옮겨주고 => 다른 화물선
  # 5개씩 빼서 작은 화물선에 추가해주는 코드를 작성해보자
  # 화물선 번호를 체크
  
  ea  = 1
  # 큰화물선이 비어잇지 않으면 반복을 한다.
  
  while not e.pcheck():
    for i in range(5):
      # 1. 큰화물선에서 화물을 하나 뺀다. => 화물을 저장할 변수가 하나 필요하다.
     #e.pop()
      o = e.pop()
      a.push(o)

      #결과값 => 몇번째 화물선인지 
      # 2. 뺀값을 작은 화물선에다가 추가해준다. 
      if o == 16:
        return ea
    ea += 1


# 함수 사용하기
print(left(cargo,carback))

# cargo 출력하기
# carback 출력하기
cargo.printc()
carback.printc()

















































































































































































































































































































































































































































































































































































































































