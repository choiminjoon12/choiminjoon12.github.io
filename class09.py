print("mission 1-------------")
route = {'a':{'b':1772,'c':5805,'f':5546,'h':730},
         'b':{'a':1772,'d':3010,'g':2562},
         'c':{'a':5805,'d':4111,'e':1081,'f':1621},
         'd':{'b':2010,'c':4111,'e':2892,'g':2908,'h':3092,'j':517},
         'e':{'c':1081,'d':2892,'f':4082,'i':506,'j':290},
         'f':{'a':5546,'c':1621,'e':4082,'i':627},
         'g':{'b':2562,'d':2908,'h':903},
         'h':{'a':730,'d':3092,'g':903,'j':3900},
         'i':{'f':627,'e':506},
         'j':{'d':517,'h':3900,'e':290}
        }


# 해당도로 삭제하기
# c-d
# c-f
# d-h
# f-e
# h-j

route['c'].pop('d')
route['d'].pop('c')

route['d'].pop('h')
route['h'].pop('d')

route['f'].pop('e')
route['e'].pop('f')

route['h'].pop('j')
route['j'].pop('h')

route['c'].pop('f')
route['f'].pop('c')


print(route)


print("mission 2-------------")
# 각 경로마다 얼마나 걸리는지가 궁금해요.


road = ['afie', 'ace', 'abde', 'abdje', 'abgde', 'abgdje', 'ahgde', 'ahgdje']

# 함수
# - 입력값 : 경로(문자열)
# - 결과값 : 총합(숫자)
def a(e):

  hapgue = 0
  # e = 'afie' 문자열의 크기 4
  # 도로 a-f, f-i, i-e 3개
  # 문자열의 크기보다 1작게 반복을 돌려보자
  for g in range(len(e) - 1):
    # 현재값, 다음값출력해보기
    # print(e[g],"-", e[g+1])
    # 라우터에서 거리 구하기
    ap = e[g]
    due = e[g+1]
    # print(route[ap][due])
    hapgue = hapgue + route[ap][due]

  return hapgue


# road안의 값을 넣어서 함수를 돌려줄겁니다. => 반복문
# 그러면 road 데이터 뽑는고 => 함수 사용하기
muukk = []
for c in range(len(road)):
  print("입력값", road[c])
  # a사용해주자. raod[c]을 넣어 사용하기(a)
  # 함수사용
  muukk.append(a(road[c])) 
  print(a(road[c]))

print(muukk)


# 최댓값 구하기

# num = [12,13,11,15,14]
# jj = 0
# for e in num:
#     if e > jj:
#         jj = e
#     print(e,jj)


print("mission3 ------------")
# muukk 가장 작은 값을 찾아라
jujang = muukk[0]
for e in muukk:
  if e > jujang:
    jujang = e
  print(e,jujang)

print("최대값",jujang)


# (과제) Mukk에서 최대값구해보기
''''''



10134