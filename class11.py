a = 172 # -민준이키
b = 160 # -선생님키
c = 143 # -다른 친구 키
e_s = 0 # -임시저장소 lee(임)em=엠 a=b, b = c , c = a,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,e_s = c

# -임시저장소의 역할은 없어지는 값을 아예 없어지기전에 보관하는 공관
e_s = c # -없어지는 값을 넣어주면 좋다
c = a
a = b
b = e_s

# print(a)
# print(b)
# print(c)

print("mission1 ------------")
# 홍채데이터 : 이차원리스트
# - 행(세로)과 열(가로)

Iris = [[0.0, 0.5, 0.1, 0.4, 0.2, 1.0, 1.0, 0.9],
   [1.0, 0.9, 0.0, 0.0, 0.1, 0.0, 0.3, 0.1],
   [0.2, 1.0, 0.1, 0.2, 0.3, 0.7, 1.0, 0.9],
   [0.9, 0.7, 0.5, 0.4, 0.2, 0.3, 0.0, 0.1],
   [0.1, 0.2, 0.3, 0.1, 0.6, 0.0, 1.1, 0.3],
   [0.4, 0.6, 0.7, 0.8, 0.0, 1.0, 1.1, 1.2],
   [0.0, 0.1, 0.1, 0.3, 0.2, 0.1, 0.8, 0.9],
   [0.0, 0.3, 0.1, 1.0, 0.9, 0.0, 0.5, 0.3],
   [0.4, 0.2, 0.1, 0.8, 0.4, 0.2, 0.3, 0.0],
   [0.7, 0.5, 0.4, 0.2, 0.0, 0.1, 0.1, 0.2],
   [0.1, 0.2, 0.1, 0.8, 0.4, 0.2, 0.8, 0.0],
   [0.0, 0.2, 0.3, 0.1, 0.6, 0.0, 0.7, 0.0]]


# [0.0, 0.5, 0.1, 0.4, 0.2, 1.0, 1.0, 0.9]
# 바뀐모습 => [0.9 1.0 1.0 0.2 0.4 0.1 0.5 0.0]


# Iris : 리스트
# - i : 행번호(숫자타입)
# - j : 열번호(숫자타입)
for i in range(len(Iris)):
   # 각행별로 
   for j in range(int(len(Iris[i]) / 2)):
      # print(Iris[i][j])
      e_s = 0
      # a = Iris[i][j]
      # b = Iris[i][len(Iris[i]) - j - 1]

      e_s = Iris[i][j]
      Iris[i][j]= Iris[i][len(Iris[i]) - j - 1]
      Iris[i][len(Iris[i]) - j - 1]= e_s

      # # 앞번호 : 현재번호
      # print(j,"/ 현재 a값", Iris[i][j])

      # # 뒷번호 : 바꿔줄 뒷번호
      # print(len(Iris[i]) - j - 1,"/ 바뀔 b값",Iris[i][len(Iris[i]) - j - 1])
      # print('--')

      #print(e)

      # print("a값",a)

   print('----------------')



print(Iris)

# 과제1 --- 
a = "서울"
b = "부산"
c = ""

c = a
a = b
b = c
print('서울 이였던',a)
print('부산 이였던',b)
# 서로의 위치를 바꿔주세요


# 과제 2 ----------
# 내부리스트의 값을 서로 반전해서 출력해주세요.
numbers=[[1,2],[1,10],[2,4],[5,6]]
# 결과 [[2,1],[10,1],[4,2],[6,5]]

for e in range(len(numbers)):
   # 내부리스트의 0번째값과 1번째값을 자리를 바꿔서 저장하고 싶다.

   # print(numbers[e])
   k = 0
   # q = numbers[e][0]  # 숫자타입을 저장한 변수
   # r = numbers[e][1]
   k = numbers[e][0] 
   numbers[e][0] = numbers[e][1]
   numbers[e][1]= k
   # print(q,r)

print(numbers)


# 리스트이 값을 바꿔보는 연습 ----
numbers =[1,2,3,4,5,6,7,8,9,10]
# 짝수값(2로 나눴을때 나머지 0인것)은 2배로 바꿔서 저장해준다.
# [1,4,3,8,5,12,7,16,9,20]
for t in range(len(numbers)):
   if numbers[t] % 2 == 0:
      print(numbers[t]*2)
      numbers[t] =numbers[t]*2
print(numbers)



# 과제 2 ----------
alphabet =[['a','b'],['c','d'],['e','f'],['g','h']]
for e in range(len(alphabet)):
   #print(alphabet[e])
   e_s = 0
   e_s = alphabet[e][0]#무슨값이 들어가면 좋을까
   alphabet[e][0] = alphabet[e][1]
   alphabet[e][1] = e_s
   print(alphabet[e])





# 과제 3 ----------
# 좌우 반전해서 출려주세요~!
numbers =[1,2,3,4,5,6,7,8,9,10] 
# 결과 = [10,9,8,7,6,5,4,3,2,1]
# 1(0)-10(-1,9) / 2(1)-9(-2,8) / 3(2)-8(-3,7) / 4-7 / 5-6 5번/ numbers크기의 절반만큼
# => 뒷번호 : len(number)-첫번째값index-1
# => 10-2-1=7

e_c = 0
for t in range(int(len(numbers) / 2)):
   #print(numbers[t])
   e_x = []
   f = numbers[t] # 첫번째값 성공
   print("첫번째값",f)
   # 바꿔줄 값 출력하기
   g = len(numbers) - t - 1 # 인덱스번호인지? 값인지? 요것만 정확하게 체크하기
   print(numbers[g])
   e_x = numbers[t]
   numbers[t] = numbers[g]
   numbers[g] = e_x
print(numbers)



print("=============과제 4==============")
alphabet = ['a','b','c','d','e','f','g','h']
           # 0,  1 , 2 , 3,  4,  5,  6,  7


# 좌우반전에서 출력해주기
for a in range(int(len(alphabet) / 2)):
   print(a,"반복변수=> 앞의 바꾸값의 인덱스번호")
   e_t = []
   b =  alphabet[a]
   print(alphabet[a])
   c = (len(alphabet)- 1) -a # h인덱스
   e_t = alphabet[a]
   alphabet[a] = alphabet[c]
   alphabet[c] = e_t
print(alphabet)





























































































































































































































































