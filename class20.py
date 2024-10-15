'''
Voice : 목소리의 속성이랑 메소드를 만들기
- 초기 속성 데이터 => 생성자에서 확인하기
     1) tone 톤
     2) pitch 피치길이
     3) Frequency 음역대
     4) speed 스피드
     5) decibel 데시벨
- 메소드 
'''
class Voice:
    def __init__(self, tone, pitch, frequency, speed, decibel):
      self.tone = tone #85~255
      self.pitch = pitch #60~300
      self.frequency = frequency #100~400Hz 
      self.speed = speed #0~500spm
      self.decibel = decibel # 50~2000
      

'''
park_info_robot 클래스
- 초기 속성데이터
 1) list : 리스트
 2) name : 이름

- 메소드
1) say_hi
'''


class ParkInfoRobot:
    def __init__(self, list, name="0"): # <- 매개변수
      self.list = list # 음성 리스트
      self.name = name # 스프라이트 이름

    def say_hi():
      print('Hi, ask me anything.')

    # 원하는 시간을 입력하면, 그시간의 음성 데이터를 출력해주는게 목적이 된다.
    # 클래스 내부 메서드는 클래스 내부데이터르 활용해야한다.
    def e(self, time):
      # 테스트: 입력한 시간 출력해보기
      # 테스트 : 객체의 리스트를 출력해주세요.
      # 리스트에서 튜플의 Key값이 time인 것중에서 vlauerk 2340이랑 같은 값의 딕셔너리를 뽑아주세요.
      for ee in range(len(self.list)):
        #print(self.list[ee])
        a = self.list[ee]
        if a["time"] == 2340:
          # a의 voice의 value출력하기
          print(a["voice"].tone,a["voice"].pitch,a["voice"].frequency,a["voice"].speed,a["voice"].decibel)
        
        


    # 원하는 시간대, 원하는 목소리를 넣어주면, 그 시간대의 음성 데터가 목소리랑 같은지 판단하기
    # 같으면 로봇 이름 출력, 다르면 "아니다" 출력하기

    
    def eeeeeeee(self,time,voice):
       for eeeeeee in range(len(self.list)):
          #print(self.list[eeeeeee])
          if self.list[eeeeeee]['time'] == time:
            # 해당값의 voice값 아져오기
            # {'time': 2050, 'voice': <__main__.Voice object at 0x000002A861A8B800>}
            #print(self.list[eeeeeee]['voice'])
            if self.list[eeeeeee]['voice'].tone == voice.tone and  self.list[eeeeeee]['voice'].pitch == voice.pitch and self.list[eeeeeee]['voice'].frequency == voice.frequency and self.list[eeeeeee]['voice'].speed == voice.speed and self.list[eeeeeee]['voice'].decibel == voice.decibel:
               print(self.name)
            
            # 딕셔너리 voice와 voice 같은지 다른지
            # - 각각의 속성 데이터을 모두 비교해서 같은지 알아보자
            #



# voice객체 속성 데이터 객체.tone
 # 1) tone 톤
 # 2) pitch 피치길이
 # 3) frequency 음역대
 # 4) speed 스피드
 # 5) decibel 데시벨

# 인스턴스 생성하기 : 객체(빵) 만들기
# - 빵만들면 생성자를 통해서 초기 데이터가 저장된다.
# - 빵만들기 생성자에 필요한 데이터 넣어줘야한다.
a = [1]
b = "bread"


# 복제본 변수이름 var e = clone()
sample_robot = ParkInfoRobot(a,b) # <- [1]리스트를 가진 "bread"라는 이름 의 로봇을 만들어준겁니다.








#voice 객체 생성부. 미션 수행시 수정하지 않습니다.
# 리스트, 딕셔너리가 있는 형태
list1 = [{'time':2050,'voice':Voice(183,70,389,196,19)},{'time':2306,'voice':Voice(214,200,230,13,54)}]
list2 = [{'time':1114,'voice':Voice(205,82,270,227,68)},{'time':1744,'voice':Voice(167,73,302,445,35)},{'time':2311,'voice':Voice(177,230,266,446,51)}]
list3 = [{'time':2250,'voice':Voice(98,191,229,208,52)},{'time':1402,'voice':Voice(109,241,197,224,33)}]
list4 = [{'time':1835,'voice':Voice(195,290,137,471,61)},{'time':1440,'voice':Voice(178,299,332,22,58)},{'time':1849,'voice':Voice(162,250,192,320,61)}]
list5 = [{'time':1728,'voice':Voice(160,285,327,439,60)},{'time':2340,'voice':Voice(156,88,212,25,52)},{'time':2340,'voice':Voice(96,268,113,170,70)}]
list6 = [{'time':1940,'voice':Voice(203,103,340,10,18)},{'time':2340,'voice':Voice(152,278,120,357,66)},{'time':1356,'voice':Voice(174,215,266,106,41)}]
list7 = [{'time':1300,'voice':Voice(103,107,258,430,19)},{'time':1413,'voice':Voice(85,80,279,30,11)},{'time':1527,'voice':Voice(116,181,248,144,22)}]
list8 = [{'time':1740,'voice':Voice(194,86,391,68,19)},{'time':1627,'voice':Voice(107,248,171,351,35)},{'time':2217,'voice':Voice(88,101,278,434,10)}]
list9 = [{'time':2340,'voice':Voice(151,270,113,170,70)},{'time':2340,'voice':Voice(152,278,120,356,66)},{'time':2405, 'voice':Voice(150,200,300,460,10)},{'time':2416, 'voice':Voice(230,152,258,200,65)}]
#voice 객체 생성부. 미션 수행시 수정하지 않습니다.


# 객체 생성
# - 생성할때 생성자의 초기 데이터를 같이 넣어줘야한다.
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.
rb_1 = ParkInfoRobot(list1, 'R1') # 리스트1이들어간 R1이름을 가진 로봇
rb_2 = ParkInfoRobot(list2, 'R2') # 리스트2이들어간 R2이름을 가진 로봇
rb_3 = ParkInfoRobot(list3, 'R3') # 리스트3이들어간 R3이름을 가진 로봇
rb_4 = ParkInfoRobot(list4, 'R4')
rb_5 = ParkInfoRobot(list5, 'R5')
rb_6 = ParkInfoRobot(list6, 'R6')
rb_7 = ParkInfoRobot(list7, 'R7')
rb_8 = ParkInfoRobot(list8, 'R8')
rb_9 = ParkInfoRobot(list9, 'R9')
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.


# 미션1 내가 원하는 시간대의 음성을 보여지게 하자
# 2340

rb_1.e(2340)
rb_2.e(2340)
rb_3.e(2340)
rb_4.e(2340)
rb_5.e(2340)
rb_6.e(2340)
rb_7.e(2340)
rb_8.e(2340)
rb_9.e(2340)


print("mission 2 ====================")

target = Voice(152, 278, 120, 356, 66)
rb_1.eeeeeeee(2340,target)

rb_1.eeeeeeee(2340,target)
rb_2.eeeeeeee(2340,target)
rb_3.eeeeeeee(2340,target)
rb_4.eeeeeeee(2340,target)
rb_5.eeeeeeee(2340,target)
rb_6.eeeeeeee(2340,target)
rb_7.eeeeeeee(2340,target)
rb_8.eeeeeeee(2340,target)
rb_9.eeeeeeee(2340,target)










