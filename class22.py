#코드 창에 아래의 코드를 입력해 보세요.
#print("안녕하세요")

# computer vision : 이미지, 비디오를 분석하는 인공지능 분야
# openCV : 얼굴인식, 문자인식, 사진 편집 등과 같은 기능을 지원하는 라이브러리

import cv2
import wizLib
import numpy

# 1. 이미지 읽는 함수 imread('파일이름')
# 2. 이미지 보여지는 함수 imshow('뉴이름','보여지는파일이름')
# 3. 이미지변경하는 함수 filter2D("대상이미지이름",옵션)
# 4. 

# numpy 모듈
#  숫자 파이=
#  R 0~255 G 0~255 B 0~255

# SY 75 1809
#number_plate.png

# 파이썬이 갖고 있을 수 있도록 이미지를 읽어
e = cv2.imread("number_plate.png")
wizLib.imshow('ee',e)

# e라는 변수에 이미지가 저장되어 있고,
# 2차원리스트로 마스크를 만들어볼때 => numpy
# 15*15 => numpy.ones((가로크기,세로크기),int)
mask = numpy.ones((15,15),int)
print(mask)

# 이미지를 가장 밝은 값으로 바꿔주는 함수
# cv2.dilate(이미지명, 마스크, iterations=횟수)
eee = cv2.dilate(e,mask,iterations = 1)
wizLib.imshow("ee",eee)













































