import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지 파일 읽기
image_path = 'day3/Lenna.png'
image = cv2.imread(image_path)

# BGR 채널 분리
b, g, r = cv2.split(image)

# 히스토그램 계산
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# 히스토그램 출력
plt.figure()
plt.title('BGR Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist_b, color='b', label='Blue')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_r, color='r', label='Red')
plt.legend()
plt.xlim([0, 256])
plt.show()