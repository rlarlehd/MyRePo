import cv2

# 이미지 읽기
image = cv2.imread('day3/Lenna.png')

# BGR에서 HSV로 색 공간 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 성분 분리
h, s, v = cv2.split(hsv_image)

# HSV 성분 출력
cv2.imshow("Hue Channel", h)
cv2.imshow("Saturation Channel", s)
cv2.imshow("Value Channel", v)

# 키 입력 대기 및 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()