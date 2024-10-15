
'''
함수 : 

'''

# def 이름(매개변수):
#   기능

# 문자랑 변수를 섞어쓰고싶은데 귀찮아서 f""

# 연도, 달, 월 입력하면
# 2024년 6월 11일 입니다. 출력해주느 함수 만들어보기
# y = 2024
# m = 6
# d = 11
# def today(e,ee,eee):
#   print(f"{e}년{ee}월{eee}일")

#프롬프트
# 입력하기 - input() 
# 입력할때 변수에 저장해줘야한다.
# name = input("이름을 입력해주세요.") 
# print("입력값 확인",name)

# Input을 사용해서 연도, 월, 일을 입력받아주세요.
# year = input("오늘은")




# 입력
# 입력받은 값을 사용하고 싶어요. => 변수
# ee = input("숫자를 입력해주세요.")

# y = 2024
# m = 6
# d = 11

# Input을 사용해서 연도, 월, 일을 입력받아주세요.
def today(e,ee,eee):
  if e == "1":
    return "이런날 없습니다."
  return f"{e}년{ee}월{eee}일"



# eaea = input("연도")
# eae = input("달")
# ea = input("일")
# e = input("시")

# print(today(eaea, eae, ea))


#  \  입력(매개변수)   /
#  -      ------------
# |       계산         |
# |                   |
#  ------------/  결과 \


# ---------------------------

# for 반복변수 in 반복조건: 


# 워밍업 : 10번 반복해서 print("hi") 외처주세요.
# - 횟수반복 : range()

# 합계구하기 : 0~9까지의 숫자의 합께를 구해보기

# for e in range(10):
#   print(" hi")
#   print(e)

# n=10일때 0~9까지의 합계






# def gsg(n):
#   e = 0
#   for eeeee in range(n):
#     # print(eeeee)
#     e = e+eeeee
#     # print(e)

#   return e

# print("0~99999합계 :",gsg(100000))


# N=10일때 1~10의함계구하기 

def gcg(n):
  jj = 0
  for aaeee in range(n):
    #print(aaeee+1)
    jj_two = aaeee + 1
    jj =  jj + jj_two
  return jj


# 1~10더한 숫자gcg(10)와 1~100(gcg(100)의 합

print(gcg(10) + gcg(100))

print("히히히히")

# '''
# 리스트 : 여러가지 데이터를 하나로 묶어놓은 데이터타입 [,,,]
# - 인데스(순서)가 있는 데이터타입이였다.

# '''

#문자열 -> 리스트 split() 문자열 내장함수
e = "a,b,c,d,e"  # 눈으로 보면 여러개 데이터 있는 것처럼보이는데 컴퓨터에서는 1개 데이터
# ,기준으로 쪼개서 리스트로 만들고 싶어요
# 문자열.split("구분인자")

print(e.split(","))


# 주어진 Numbers 리스트의 합계를 구해볼겁니다.
numbers = [1,2,3,4,5,10,11,12,13,14,15]
# 리스트에 있는 값을 모두 뽑고싶으면 반복문을 사용해야한다.

# 반복1번째 : 리스트롤 통째로 반복돌릴수 있다. => 순서알수없지만, 리스트안의 값을 바로 알수가 있다.
for bb in numbers:
  print(bb)

print("---리스트반복2번째 ---")
# 반복2번째 : range() 
# 리스트의 크기만큼 range로 반복을 돌리면 된다.
# bb에는 인덱스(순서)가 들어간다.
jj = 0
for bb in range(len(numbers)):
  print(numbers[bb]) 
  jj = numbers[bb] + jj

#
print("---반복문 & 조건문 ---")
# 주어진 Numbers 리스트에서 10이상인 수의 합계를 구해볼겁니다.
numbers = [1,2,3,4,5,10,11,12,13,14,15]
i_n = 0
#####순서
for ban_bok in range(len(numbers)):
  #print(ban_bok)
  if numbers[ban_bok] >= 10:
    i_n = numbers[ban_bok] + i_n
print(i_n)


# 반복문 흐름을 제어하는 역할
# break: 반복문을 중간에 그만~~~
# continue : 다음 반복으로 이동하기

#----------------
# 주어진 Numbers 리스트에서 10이상인 수의 합계를 구해볼겁니다.
# continue :만들어보기
###같은------ㅣ

ju_jang = 0
for bb in numbers:
  #print(bb)
  #조건은 numbers 안에있는 값이 10보다 낮을때 continue를 쓰고 그 이후로는 다 더한다
  if bb < 10:
    continue
  ju_jang = ju_jang + bb


print(ju_jang)




