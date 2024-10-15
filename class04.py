# 리스트 []
# - 인덱스(순서)가 있다.

# alphabet = ["a","b","c","d",'e',"f","g"]
# # 반복 for문
# # 1. range() - 인덱스를 활용하는 방법
# # - 인덱스(i), 리스트의 값도 알수있다.
# for al in range(len(alphabet)):
#   print(al)
#   print(alphabet[al])
#   print('----------')

# print('>>>>>>>>>>>>>>>')

# 2. 인덱스없이 리스트 자체를 반복시키기
# - 바로 리스트의 값을 사용할수가 있었다.
# for alpha in alphabet:
#   print(alpha)


'''
딕셔너리 {"key":"value"} **
- 인덱스가 없어요. 대신 "key"가 있다.
- 딕셔너리변수["key"], 딕셔너리변수.get("key")

- 딕셔너리.keys() : 키 값만 가져오기
- 딕녀서리.values() : value값들만 가져오기
- 딕셔너리.items() : (key,value) 튜플 형태로 나온다.

'''
# 아이스크림 변수에 키 이름으로 아이스크림 , value 가격을 넣어주세요. 
icecream = {"미니 누가바":7000,"붕어싸만코":2200,"스크류바":1500}
print(icecream["미니 누가바"])




# 예제 : icecream 딕셔너리의 총 가격을 함수로 작성해주세요.
# 입력값은 딕셔너리
# 출력값 합계(숫자)
# jj = 0
# for k,v in icecream.items():
#   jj = v + jj
# print(jj)

def hg(e):
  jj = 0
  for k,v in e.items():
    jj = v + jj
  return jj

print(hg(icecream))


# 딕셔너리 + 리스트
# 아이스크림  키로 아이스크림 이름 value [가격, 갯수]
icecream2 = {"미니 누가바":[7000,2],
             "붕어싸만코":[2200,3],
             "스크류바":[1500,10]}

# 아이스크림의 이름과 가격, 수량 딕셔너리의 몇개 구매햇는지를 함수로 궁급하니다.
# 입력값 딕셔너리
# 출력값은 갯수의 합계(숫자)
def e(ice):
  # print(ice["미니 누가바"][1])
  h = 0
  for ke,val in ice.items():
    # print(val[1])
    h += val[1]
  return h 

print(e(icecream2))


icecream2 = {"미니 누가바":[7000,2],
   "붕어싸만코":[2200,3],
   "스크류바":[1500,10]}
# 몸풀기 : # 아이스크림의 이름과 가격, 수량이 있다. icecream2 담긴 아이스크림들의 총 가격을 구하는 함수를 만들어주세요.
# 저장하는 변수 = jj 가격 = b, 수량 = c라고 할떄 jj = a * b 
print(">>>>")
def gcg(p):
  jj = 0
  for e,a in p.items():
    print(e,a)
    b = a[0]
    c = a[1]
    print(b*c)
    jj += b*c
  return jj


print(gcg(icecream2))

print(">>>>")
# 딕셔너리의 최종최종최종 
# 리스트 + 딕셔너리
icecream3 = [
  {"이름":"미니 누가바", "가격": 7000, "수량":2},
  {"이름":"붕어싸만코", "가격": 2200, "수량":3},
  {"이름":"스크류바", "가격": 1500, "수량":10},
  {"이름":"메로나", "가격":800, "수량": 5}
]

# 아이스크림냉동고에 icecream3 진열되어있다. 이중에서 메로나와 스크류바를 모두 구매할때 가격이 어떻게 되는가 함수로 만들어주세요.
def cold(t):
  gj = 0
  for e in t:
    #print(e['이름'])
    if e['이름'] in ["스크류바","메로나"]:
      print(e['가격'])
      gj += e["가격"] * e["수량"]
  return gj

print(cold(icecream3))


print(icecream2.items())
'''
튜플(tuple) :  ()
- 리스트랑 동일하다. 
- 수정할수 있으면 리스트, 수정할수 없으면 튜플
- zip : 두개의 리스트나 합치기 => 튜플로 만들어요



'''
# ('미니 누가바', [7000, 2])
# ('붕어싸만코', [2200, 3]) 
# ('스크류바', [1500, 10])

icecream4 = [
  '미니 누가바',
  '붕어싸만코',
  '스크류바'
]
icecream_price = [
  7000,
  2200,
  1500
]

for value in zip(icecream4,icecream_price):
  print(value)



'''
집합 set() {}
- 순서 없다.
- 중복이 없어요.

'''
test1 = {"a","a","a","b","b","c","e"}
test2 = {"a","a","a","b","b","c","d"}
print(test2-test1)

# 교집합 &
# 합집합 |
# 차집합 -

















































