# 클래스 : 객체(object)의 틀(속성(데이터) , 메소드(함수)) 만들기
# 생성자 def __init__(self)
# => 객체를 만들때, 초기 속성(데이터)값을 만들어주는 역할을 한다.
# 





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
