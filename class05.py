# 대학생 형아 누나도 어렵다...
# 이차원리스트
# - 행:(세로, 줄)
# - 열:(가로, 칸)
# - 이차원리스트의 크기 = 5(열의크기)*4(행의크기)

numbers= [
#0번열, 1번열,2번열,3번열 ,... 
  [1 ,2 ,3 ,4 ,5 ],  # 행 0번
  [6 ,7 ,8 ,9 ,10],  # 행 1번
  [11,12,13,14,15],  # 행 2번
  [16,17,18,19,20],
]

# 1행 2번째 8

# 이차원리스트에서 값을 뽑을때
# 변수이름[행의번호][열의번호]

print(numbers[0][4])

# 이차원리스트도 모든 값을 뽑아보고싶다~!
# => 이중 for문

for ee in numbers:
  # 내부리스트의 값을을 출력하고 싶다.
  # => 한번더 반복문을 할수가 있다!
  #print(ee)
  for eee in ee:
    print(eee)

# range()로 바꿔주세요!

numbers= [
#0번열, 1번열,2번열,3번열 ,... 
  [1 ,2 ,3 ,4 ,5 ],  # 행 0번
  [6 ,7 ,8 ,9 ,10],  # 행 1번
  [11,12,13,14,15],  # 행 2번
  [16,17,18,19,20],
]

[1 ,2 ,3 ,4 ,5 ]

# print(len(numbers))
for i in range(len(numbers)):
  # print(i,"행번호 ----")
  for j in  range(len(numbers[i])):
    print(numbers[i][j])



# 퀴즈1번 2차원리스트를 만들어보기
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# 이 num_list 2개씩 잘라서 2차원리스트로 만들어주세요!
result =[
  [1, 2], 
  [3, 4], 
  [5, 6], 
  [7, 8]
]
print("-----------------------------------------------------------------------------------------")
g = []
for eeee in range(0,len(num_list)-1,2):
  print(num_list[eeee])
  g.append([num_list[eeee],num_list[eeee+1]])

print(g)

# range(start,end,step)




# 이차원리스트의 탐색
alphabet =[
  ["a","b","c","d","e"],
  ["f","g","h","i","j"],
  ["k","l","m","n","o"],
  ["p","q","r","s","t"],
  ["u","v","w","x","y"],
]

# m : 2번째 행, 2번째열
# m의 위 값 : "h" 1번째 행(-1) 2번째열(똑같다.)
# m의 아래값 : "r" 3번째 행(+1), 2번째열(똑같다)
# m의 왼쪽값 : "l" 2번째 행(행은똑같다), 1번째열(-1)
# m의 오른쪽값 : "n" 2번째 행(행은똑같다), 3번째열(+1)



# g의 값을 찾아서 출력해주세요
print(alphabet[1][1])
print("위의값",alphabet[0][1])
print("아래값",alphabet[2][1])
print("왼쪽값",alphabet[1][0])
print("오른쪽값",alphabet[1][2])

i = 3 #행의값
j = 2 #열의값

print(alphabet[i][j])
print("위의값",alphabet[i-1][j])
print("아래값",alphabet[i+1][j])
print("왼쪽값",alphabet[i][j-1])
print("오른쪽값",alphabet[i][j+1])

야호


