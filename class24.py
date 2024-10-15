


print("mission 로봇이 도청기를 설치하기 위한 경로를 탐색하기")
# route : 이차원리스트 맵
# - 0 : 길
# - 1 : 벽
# - 2 : 도착
route= [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 2],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0]
]
# 현재 위치 # 행 : i / 열 : j
i = 0
j = 0

# 언제까지 경로를 돌아다니면 되지? i,j의 값이 2일때까지 반복돌리면된다.
# 경로(route)에서 현재위치(i번째 행 , j번째 열)의 값이 2가 되지않으면 반복돌리자.
# 위 N / 아래 S / 왼쪽으로 W / 오른쪽 E 
le = []


while route[i][j] != 2:
    # 위를 볼때의 특징 : 위의 값이 0보다 커야한다.
    # 현재가 2번이면 위의 행은 1번  / 현재가 i번이면 위의 값 i-1
    if i - 1 >= 0:
        # 위 위치의 값이 0이 될때 이동하기
        if route[i-1][j] == 0:
            route[i][j] = 3
            i = i - 1
            print('N')
            le.append('N')
            continue
        # 2번째 조건으로 이후 값이 2이면 프린트 해주고 끝내면 됩니다. 
        elif route[i - 1][j] == 2:
            le.append('N')
            break
            
        
    # 아래 볼때의 특징 : 아래값(i+1)이 리스트의 크기보다 작아야한다.
    if i + 1 < len(route):
        if route[i + 1][j] == 0:
            route[i][j] = 3
            i = i + 1
            print("S")
            le.append('S')
            continue
        elif route[i + 1][j] == 2:
            le.append('S')
            break
    
    # 왼쪽볼때의 특징 : 왼쪽(j-1)보다 커야한다.
    if j - 1 >= 0: 
        if route[i][j - 1] == 0:
            route[i][j] = 3
            j = j - 1
            print("W")
            le.append('W')
            continue
        elif route[i][j - 1] == 2:
            le.append('W')
            break

    # 오른쪽 볼때의 특징 : 오른쪽으니 행리스트의 크기보다 작아야합니다.
    if j + 1 < len(route[i]):
        if route[i][j + 1] == 0:
            route[i][j] = 3
            j = j +1
            print("E")
            le.append('E')
            continue
        elif route[i][j + 1] == 2:
            le.append('E')
            break

# 끝나면 2니깐 
print(le)


# 클래스로 스택을 만들어볼겁니다.
# 데이터: 리스트
# 메소드 - push
#      - pop
#      - 제일 위에있는 값이 뭔지 알려주는 함수 만들기
#      - 비어있는 스택인지 알려주는 함수


# stack / queue
route= [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 2],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0]
]
# 현재 위치 # 행 : i / 열 : j
i = 0 
j = 0
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

staack = Stack([])


while route[i][j] != 2:
    # 위를 볼때의 특징 : 위의 값이 0보다 커야한다.
    # 현재가 2번이면 위의 행은 1번  / 현재가 i번이면 위의 값 i-1
    if i - 1 >= 0:
        # 위 위치의 값이 0이 될때 이동하기
        if route[i-1][j] == 0:
            route[i][j] = 3
            i = i - 1
            print('N')
            # // 여기서 방향을 알수가 있다.\
            staack.push('N')

            # 방향을 추가하는 곳 
            
            continue
        # 2번째 조건으로 이후 값이 2이면 프린트 해주고 끝내면 됩니다. 
        elif route[i - 1][j] == 2:
            staack.push('N')
            break

    # 아래 볼때의 특징 : 아래값(i+1)이 리스트의 크기보다 작아야한다.
    if i + 1 < len(route):
        if route[i + 1][j] == 0:
            route[i][j] = 3
            i = i + 1
            staack.push('S')

            continue
        elif route[i + 1][j] == 2:
            staack.push('S')
            break
    
    # 왼쪽볼때의 특징 : 왼쪽(j-1)보다 커야한다.
    if j - 1 >= 0: 
        if route[i][j - 1] == 0:
            route[i][j] = 3
            j = j - 1
            staack.push('W')
            continue
        elif route[i][j - 1] == 2:
            staack.push('W')
            break

    # 오른쪽 볼때의 특징 : 오른쪽으니 행리스트의 크기보다 작아야합니다.
    if j + 1 < len(route[i]):
        if route[i][j + 1] == 0:
            route[i][j] = 3
            j = j +1
            staack.push('E')
            continue
        elif route[i][j + 1] == 2:
            staack.push('E')
            break


staack.printc()






































