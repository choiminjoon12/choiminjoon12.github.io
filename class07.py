print("mission 1--------------------")
# 출발 9
# 도착 5
# 길 0
# 별 1 


# 위 N 아래 S 왼쪽 W, 오른쫃 E
# 방향을 저장해줄 비어있는 리스트 변수가 필요하다
banghuang = []


route= [
[1,9,1,1,1,1,1,1],
[1,0,1,0,0,0,0,1],
[1,0,0,0,1,1,0,1],
[1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1],
[1,0,0,0,0,0,0,5],
[1,1,1,1,1,1,1,1]
]


# 출발지의 위치를 체크하기
# - route에서 "9"의 행의 번호 i, 열의 번호 j 를 찾아야한다.

# 행번호 변수 
# 열번호 변수0


heng = 0  # 현재위치의 행값
yeol = 0  # 현재위치의 열값

# 이차원리스트 모든 값에 대해서 접근하려면 이중For문을 사용해야한다.
# 행의 번호 i, 열의 번호 j가 중요한 미션들이 많아요. range사용한다.
# 

print("행의 크기",len(route),"줄", "리스트가 몇개인가?")
print("열의 크기",len(route[0]),"칸", "리스트(한줄)안의 숫자가 몇개인가?")
print("--------------------")

for i in range(len(route)):
  # print("행번호",i)
  for j in range(len(route[i])):
    # print("--- 열번호",j)
    # print(route[i][j])
    if route[i][j] == 9:
      heng = i
      yeol = j

print("출발지의 i,j", heng,yeol)


# 출발지부터 ~~~ 현재위치의 값이 5가 될때까지 반복해서 탐색을 할거다.
# 횟수(for문)가 정확하지않을때 조건으로 반복(while)돌리면된다.


# print(route[0])


'''  
1. 무조건을 계속 반복
2. 현재위치가 5가되면
   그때 "도착" 출력해주고, 반복을 탈출한다.
'''
# 임의 - 문한반복 방지

while route[heng][yeol] != 5:


  # if route[heng][yeol] == 5:
  #   print("도착")
  #   print("*** 결과 방향 :",banghuang)
  #   break

  # print("\n===============\n")
  # print("현재 위치","행", heng,",열", yeol, "/현재 값", route[heng][yeol])
  # print(route)


  # 리스트 탐색 (위,아래,좌,우)


  #1. 위의 값 탐색
  #- 맨 윗줄이면, 위의 값을 찾을 수 없다.
  #- 찾는 조건 맨위줄이아니면 위의값 찾으면된다.
  if heng > 0:
    print("-- 위 값",route[heng - 1][yeol])
    if route[heng -1][yeol] == 0 or route[heng -1][yeol] == 5:
      print(">>>>>>","위로 이동")
      # 1.지나간 자리(현재위치)를 2번으로 바꾸고 표시 해줄겁니다.
      # 2.현재위치를 heng,yeol 다음 이동할 위치로 변경하기
      # 3.비어있는리스트(banghuang)에 방향을 추가해주기
      route[heng][yeol] = 2
      heng = heng -1
      yeol = yeol # 안적어도 된다. 헷갈리지말것
      banghuang.append("N")
      continue


  #2. 아래 값 탐색
  if heng < len(route)-1:
    print("-- 아래 값",route[heng + 1][yeol])
    if route[heng + 1][yeol] == 0 or route[heng + 1][yeol] == 5:
      print(">>>>>>","아래로 이동")

      route[heng][yeol] = 2
      heng = heng +1
      yeol = yeol # 안적어도 된다. 헷갈리지말것
      banghuang.append("S")
      continue


  #3. 왼쪽 값 탐색
  if yeol > 0:
    print("-- 왼쪽 값",route[heng][yeol -1])
    if route[heng][yeol -1] == 0 or route[heng][yeol -1] == 5:
      print(">>>>>>","왼쪽으로 이동")
      route[heng][yeol] = 2
      heng = heng # 안적어도 된다. 헷갈리지말것
      yeol = yeol -1
      banghuang.append("W")
      continue

  #4. 오른쪽 값 탐색
  if yeol < len(route[heng])-1:
    print("-- 오른쪽 값",route[heng][yeol +1])
    if route[heng][yeol +1] == 0 or route[heng][yeol +1] == 5:
      print(">>>>>>","오른쪽으로 이동")

      route[heng][yeol] = 2
      heng = heng # 안적어도 된다. 헷갈리지말것
      yeol = yeol +1
      banghuang.append("E")
      continue




print("*** 결과 방향 :",banghuang)








'''
반복문 2개 for문 / while문
- 횟수 반복 for문 : range(), 리스트(리스트크기만큼 반복)
- *조건*이 만족할때까지 반복 : while
  - 조건 설정이 잘못되면 계속 반복하면 무한반복에 빠질수 있다.
  - 무한반복문 빠지면, 망한다.
  - while문 옆 조건, if 조건: break 문 같이 활용해서 확실하게 탈출 할수 이도록 하기

while 조건:
  반복 코드
'''


