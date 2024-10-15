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



print("경로를 이탈하여 재검색합니다.")

def eeeee(gl):
  # afie (문자갯수)
  # 도로갯수 a-f,f-i,i-e (len(gl)번)
  # print(len(gl) - 1)
  for eeee in range(len(gl)-1):
    print("시작",gl[eeee],"끝",gl[eeee+1])




eeeee(road[0])







































