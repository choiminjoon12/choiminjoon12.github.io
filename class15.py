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
##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.\
# 2ㅣ2 print(bin())

ee = ""
for e in range(len(painting1)):
    jj = ['0b']
    for h in range(len(painting1[e])):
        #print(painting1[e][h].red,'1')
        #print(bin(painting1[e][h].red))
        bv = bin(painting1[e][h].red)
        #print(bv[-1])
        jj.append(bv[-1])
    #print(int("".join(jj),2))
    #print(chr(int( "".join(jj),2 )))
    ee += chr(int( "".join(jj),2 ))
print(ee)


# 문자열을 -> 리스트 : 문자열변수.split("구분인자")
# "a,b,c,d" => ['a','b','c','d']
# 리스트 -> 문자열 : 4글자: "".join(리스트변수)
print("=======")
eee = ""
for a in range(len(painting2)):
    jjj = ['0b']
    for g in range(len(painting2[a])):
        #print(painting2[a][g].red,'2')
        #print(bin(painting2[a][g].red))
        sc = bin(painting2[a][g].red)
        #print(sc[-1])
        jjj.append(sc[-1])
    #print(int( "".join(jjj),2 ))
    #print(chr(int( "".join(jjj),2 )))
    eee += chr(int( "".join(jjj),2 ))
print(eee)







