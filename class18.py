'''
객체지향프로그래밍
=> OOP

객체(object): 속성(데이터, 변수), 행동(함수)
=> 객체를 만드는 틀 : 클래스

self: 클래스 첫번째 매개변수
= 객체 자기 자신을 의미한다.

class 클래스명:
  => 클래스명은 앞글자가 대문자
  => 함수 소문자() 헷갈리지말라고 클래스명은 앞글자는 무조건 대문자

  def __init__(self): # 생성자: 초기 속성(데이터) 만드는 곳

  def 클래스내부함수(self) # 메소드 : 클래스 내부의 함수


*인스턴스 : 클래스 틀로 찍은 객체
인스턴스변수명 = 클래스명()
인스턴스변수명.메소드명()

'''


# 1. 기본클래스
# class Robot:
#   def __init__(self):
#     self.name = 'C'

#   # 로봇의 이름을 출력해주는 메소드(함수) 만들기
#   def e(self):
#     print(self.name)

# myrobot = Robot()
# myrobot.e()


# 2. 클래스 생성할때 입력값을 넣어주기
class Robot:
  def __init__(self,r):
    self.name = r

  # 로봇의 이름을 출력해주는 메소드(함수) 만들기
  def e(self):
    print(self.name)

  # 시험점수를 넣으면 90점은 A, 80점이상은 B, 나머지는 F

#박스 나르기
  def eeeeeeeeee(self,p):
    # p # 점수
    if p.grade >= 90:
      print(p.name,'A')
    elif p.grade >= 80:
      print(p.name,'B')
    else :
      print(p.name,'F')

class Student:
  def __init__(self,name,grade):
    self.name = name
    self.grade = grade


myrobot = Robot("나봇")
myrobot.e()
p_c_robot = Robot('기계')
# p_c_robot.eeeeeeeeee(124)
teacher_robot = Robot("선생님봇")
teacher_robot.e()
hak_seang = Student('민준',100)
hak_seang1 = Student('길동',35)
hak_seang2 = Student('철수',95)
print(hak_seang.name,end = "")
print(hak_seang.grade)


print(hak_seang1.name,end = "")
print(hak_seang1.grade)


print(hak_seang2.name,end = "")
print(hak_seang2.grade)

teacher_robot.eeeeeeeeee(hak_seang)
teacher_robot.eeeeeeeeee(hak_seang1)
teacher_robot.eeeeeeeeee(hak_seang2)
# Student 클래스를 사용해서 민준, 길동, 철수 학생의  인스턴스 만들어보기 
#100   35   95
# teacher 로봇한테 채점해달라고 하자


print("mission 1============")


#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")
class Server:
    def __init__(self):
        # NIS server를 이용해 통신 할 수 있는 transmitter 리스트
        self.trm_list = []
        #각 주파수 별로 현재 전파되고 있는 메시지
        self.msg_list = [None,'Hi there','>>#=@.......$#^','2_8_...M..{{{#','243','today\'s news broadcasting.','this is NIS server','%$#&^#^','Input secret code.','@*DW)R_#IO-','#$$$@__&*$%','+)@!((^@',';nNiIssssss023;','16837','\sdkf','...Hel*^%-!Pp....','call with a secret code','wewrh','service location','add user','not now','commercial zone','438759234','/32.1/2/','&*)','q3284023','.....','add transmitter','....008800888','fire','438759234','baseball','&*)','q3284023','.....','........','no excuses','hey','...bal','/32.1/2/','2375','000','.....']

    # 클래스 내부 함수 => 메소드
    # 사용자 추가하는 메소드 메서드(등록)
    def addUser(self, t, c):
        #  t : transmitter 인스턴스 / c: 유저 이름
        self.trm_list.append(t)
        print('New user', c ,'added.')

    # 사용자 삭제하는 메소드 메서드(삭제)
    def delUser(self, id):
        for i in range(len(self.trm_list)):
            if self.trm_list[i].id == id:
                del self.trm_list[i]
        print('delete completed.')

    # 메세지를 발송해주는 메서드
    def emitMsg(self, msg):
        for freq in self.msg_list:
          freq = msg

    # 서버클래스에 message 메서드 추가할겁니다.
    #- 주파수수가 15일때만 메세지가 나가도록 해주기
    def message(self,t ,freq):
      # print(freq)
      if freq == 15:
        print(self.msg_list[freq])


class Transmitter: # 서버가 송신할 정보를 저장하는 클래스
    def __init__(self, id):
       # 고유주파수 id, 주
       #
        self.id=id
        self.freq = 5 #주파수        
        print('Transmitter', id,'enrolled.')

    # 주파수 바꾸기
    def changeFreq(self, server, newFreq):
      # 서버클래스의 인스터를 입력값, 새로운 주파수 
      if newFreq <= len(server.msg_list):
        self.freq=newFreq
        print('Frequency set to', newFreq, 'completed.')
      else:
        print('Invalid Frequency.')

    #보내는 메서드
    def send(self, server, msg):
        server.msg_list[self.freq] = msg

    # 주파수로 서버에 연결해주는 메서드
    def connect(self, server):
        server.message(self, self.freq)



# 1. 서버 인스턴스를 만들기 (Server 클래스 활용)
# 2. 무전기(통신) 인스턴스 만들기(Transmitter 클래스 활용)
# - 서버 통신번호(id) 19004
# - 요원 통신번호(id) 60827
# 3. 서버에 유저를 등록해줄겁니다.
# 4. 요원, 마스터의 주파수를 15로 변경해주세요.

ss = Server() # 서버(클라우드)
a = Transmitter(60827) # 요원(공유받을사람)
s = Transmitter(19004) # 마스터(주인)
ss.addUser(a,"blue_whale")
ss.addUser(s,'master')
s.changeFreq(ss,15)
a.changeFreq(ss,15)

a.connect(ss)
# s.connect(ss)


# ...Hel*^%-!Pp....











































































































































































































































































































































































