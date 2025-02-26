import cv2
# 이미지를 읽기
image = cv2.imread('day3/Lenna.png')
# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # BGR에서 HSV 색 공간으로 변환
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    # HSV 성분 분리
    y, u, v = cv2.split(yuv_image)
    # 각각의 성분 출력
    print("Hue Component:")
    print(y)
    print("\nSaturation Component:")
    print(u)
    print("\nValue Component:")
    print(v)
    # 이미지 윈도우로 확인 (필요한 경우 사용)
    cv2.imshow('Original Image', yuv_image)
    cv2.imshow('y Image', y)
    cv2.imshow('u Image', u)
    cv2.imshow('v Image', v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

