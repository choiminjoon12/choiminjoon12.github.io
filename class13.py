'''
클래스 Class
- 객체(object) : 게임개발했을때 복제가 가능한 원본이랑 같은 의미
- 클래스를 만든다 : 복제가능한 형태의 원본을 만든다 라는 뜻이다.
- 데이터와 함수를 동시에 갖고 클래스 이다.



class 클래스이름(앞을자 대문자):
  # 클래스를 만들때 초기값을 넣어주는 생성자 메소드
  def __init__(self):
    # self : 클래스 자기 자신을 의미한다.
    # 클래스안의 변수입니다. : 다른 변수와 다릅니다라고 표현하기
    self.변수이름 = ""


# 원본으로 복제본들 만드는 것을 인스턴스instance
인스턴스변수이름(=JS복제본이름) = 클래스명()


'''

# 책
class Book:
  def __init__(self):
    self.ju_ja ="이승준"
    self.je_mok ="노마드 비즈니스맨"
    self.chul_pan_sa = "나비의 활주로"

  # 책 저자와 제목을 출력해주는 함수 만들기
  def e(self): 
    print(self.je_mok)
    print(self.ju_ja)

# 입력값이 있는 클래스
class Vook:
  def __init__(self,ee,eee,eeee ):
    self.ju_ja = ee
    self.je_mok =eee
    self.chul_pan_sa = eeee

  # 책 저자와 제목을 출력해주는 함수 만들기
  def e(self): 
    print("제목:",self.je_mok)
    print("저자:",self.ju_ja)

chek = Book()
chek.e()

chek3 = Vook('파이썬 알고리즘','박상길','교보문고')
chek3.e()

chek2 = Vook('ab','cd','ef')
chek2.e()
# 밖에서는 self. 접근 못합니다.









# 데이터 : :(책등,앞표지>:,*저자*,*제목*,*출판사*,가름끈
# 행동 : 읽기,덮기,펴기
#[]<--------


#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

class pixel:
    def __init__(self, r, g, b):
        self.red=r
        self.green=g
        self.blue=b



##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.
import random
import copy
random.seed(16)
paintingsample = [[0]*8 for i in range(8)]
for i in range(8):
  for j in range(8):
   paintingsample[i][j]=pixel(random.randint(0,255), random.randint(0,255), random.randint(0,255))
painting1=copy.deepcopy(paintingsample)



##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.
pic1 = copy.deepcopy(painting1[0])
pic1[0].red = 0
pic1[1].red = 1
pic1[2].red = 0
pic1[3].red = 0
pic1[4].red = 0
pic1[5].red = 0
pic1[6].red = 1
pic1[7].red = 1
pic2 = copy.deepcopy(painting1[1])
pic2[0].red = 0
pic2[1].red = 1
pic2[2].red = 1
pic2[3].red = 0
pic2[4].red = 1
pic2[5].red = 1
pic2[6].red = 1
pic2[7].red = 1
pic3 = copy.deepcopy(painting1[2])
pic3[0].red = 0
pic3[1].red = 1
pic3[2].red = 1
pic3[3].red = 0
pic3[4].red = 0
pic3[5].red = 1
pic3[6].red = 0
pic3[7].red = 0
pic4 = copy.deepcopy(painting1[3])
pic4[0].red = 0
pic4[1].red = 1
pic4[2].red = 1
pic4[3].red = 0
pic4[4].red = 0
pic4[5].red = 1
pic4[6].red = 0
pic4[7].red = 1
pic5 =copy.deepcopy(painting1[4])
pic5[0].red = 0
pic5[1].red = 0
pic5[2].red = 1
pic5[3].red = 0
pic5[4].red = 1
pic5[5].red = 1
pic5[6].red = 0
pic5[7].red = 1
pic6 =copy.deepcopy(painting1[5])
pic6[0].red = 0
pic6[1].red = 1
pic6[2].red = 0
pic6[3].red = 1
pic6[4].red = 1
pic6[5].red = 0
pic6[6].red = 0
pic6[7].red = 0

pic7 = copy.deepcopy(painting1[6])
pic7[0].red = 0
pic7[1].red = 1
pic7[2].red = 0
pic7[3].red = 0
pic7[4].red = 1
pic7[5].red = 1
pic7[6].red = 1
pic7[7].red = 1
pic8 = copy.deepcopy(painting1[7])
pic8[0].red = 0
pic8[1].red = 1
pic8[2].red = 0
pic8[3].red = 1
pic8[4].red = 0
pic8[5].red = 0
pic8[6].red = 1
pic8[7].red = 0
painting2=[]*8
painting2.append(pic1)
painting2.append(pic2)
painting2.append(pic3)
painting2.append(pic4)
painting2.append(pic5)
painting2.append(pic6)
painting2.append(pic7)
painting2.append(pic8)
##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.

for i in range(len(painting1)):
    #print(painting1[i])
    for j in range(len(painting1[i])):
        # red,
        # blue
        # green
        # painting1 의 Rgb
        print("rrrrrr",painting1[i][j].red)
        print("gggg",painting1[i][j].green)
        print("bb",painting1[i][j].blue)

        # painting2 rgb
        print('1----------------------------------------')
        print("rrrrrr",painting2[i][j].red)
        print("gggg",painting2[i][j].green)
        print("bb",painting2[i][j].blue)
        print('2----------------------------------------')

        if painting1[i][j].red != painting2[i][j].red:
            print("--------------------------------------------빨간색이 다르다.")
        if painting1[i][j].green != painting2[i][j].green:
            print("-----------------------------------------------초록색이 다르다.")
        if painting1[i][j].blue != painting2[i][j].blue:
            print("----------------------------------------------------파란색이 다르다.")






















































































































































































































































































































































































































































































































































































































































































































































































































