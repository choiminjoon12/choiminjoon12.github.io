#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")
'''
클래스: 만들고싶은 형태, 틀
- 인스턴스(JS게임 복제)
- 데이터(변수), 행동(함수)
'''
class el:
    def __init__(self, a, b):
        self.name = a
        self.title = b

    def e(self):
        print(self.name)
        print(self.title)



# 
name = el('l', 'l')  
name.e()



# 숫자를 -> 문자로 바꿔보자

print(ord("a"))
print(chr(96),chr(96),chr(104),chr(105),chr(96),chr(96))

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
jj= []
juj = []
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
            jj.append(painting1[i][j].red)
            juj.append(painting2[i][j].red)
        if painting1[i][j].green != painting2[i][j].green:
            print("-----------------------------------------------초록색이 다르다.")
            jj.append(painting1[i][j].green)
            juj.append(painting2[i][j].green)
        if painting1[i][j].blue != painting2[i][j].blue:
            print("----------------------------------------------------파란색이 다르다.")
            jj.append(painting1[i][j].blue)
            juj.append(painting2[i][j].blue)            
print(jj)
print(juj)

# bin : 2진수 문자열로 바꾸기
# 마지막값을 쭉 연결해서 2진수로 만들어보기
juuujang = "0b"

# for e in range(len(jj)):
#     a = bin(jj[e])
#     print(a[-1])
#     juuujang += a[-1]

for i in range(len(painting1)):
    juuujang = "0b"
    for j in range(len(painting1[i])):
        a = bin(painting1[i][j].red)
        juuujang += a[-1]
    print(chr(int(juuujang,2)))

# 10진수 바꾸기 int(2진수, 2)
# print(juuujang)
# print(int(juuujang, 2))            
# z = int(juuujang, 2)
# print(chr(z))