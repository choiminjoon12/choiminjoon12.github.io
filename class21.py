#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요"

'''
모듈: 파이썬 기본기능외에 밖에서 만든 기능을 가져와서 쓰는 것을

'''
# 
# - 수학모듈  
# yei

#모듈 가져오기 
import math
#https://docs.python.org/ko/3/library/math.html
# * 올림, 내림 *
# * 중학교때 절대값 * 
# 고등학교 때 배우는 수학적인 내용들이 지수, 로그

# 랜덤에 관련된 기능들이 있는 랜덤 모듈도 있습니다.
import random
# 모듈이름.함수()
# https://docs.python.org/ko/3/library/random.html
# random.seed(a=None, version=2)

# 0~1사이의 랜덤한 숫자 뽑아주기
print(int(random.random()*100))
# random.randrange()
print(random.randrange(1, 45))
# 37 20 42 5
# 리스트가 주어지고, 그중에서 뽑아로 하기

'''
로또 번호 뽑기 프로그램 by민준 ------------
- 1~45번 중에서 중복없는 6개 번호 뽑기
'''

ee = 6

# 반복을 돌려서 저장하고, 만약에 안에 있는 수가 있으면, 한번 더 돌린다.
# 언제까지 반복하기 6개 다 뽑힐때까지 반복돌리면 되겠죠~!
# for문 말고, while문


# for e in range(ee):
#     if eee == 
#     ilst.append(random.randrange(1, 45))
# print(ilst)
# while 조건:
  # // 조건 : 비교, 포함, 논리 등..
  # // 조건이 만족하면 반복이 돌아간다.
  # // 로또는 갯수가 6되기 전까지 뽑는다.
  # len(ilst) = 6



eee = random.randrange(1, 45)   # 1번뽑아요.
#리스트 안에있는 수가 추가하려는 수와 같다면 넣으려는 수를 빼고----
ilst =[]
while len(ilst) < 6: # 반복조건
  # 1. 내가 추가하려는 숫자가    2. 리스트안에 없다면      3. 추가한다.
  # (리스트안에 포함되어 있으면, 추가 안할거다. )
  
  # 1. 추가하고 싶은 숫자의 변수를 만들어서 저장해주자.
  eeee = random.randrange(1, 45)  # 반복이 돌아갈때 마다 뽑는다.

  # 2. 뽑은 숫자가 리스트안에 없을때(포함연산자), 
  if eeee not in ilst:
    # 3. 리스트안에 추가해준다.
    ilst.append(eeee)
print(ilst)

    
  # if ilst[len(ilst)] :
     

  



