import cv2
import numpy as np

# Open the video file
# Change to your ---
cap = cv2.VideoCapture('---')


#########################################################################
# 영상 저장
# 정수 형태로 변환하기 위해 round
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # 카메라에 따라 값이 정상적, 비정상적

# fourcc 값 받아오기, *는 문자를 풀어쓰는 방식, *'DIVX' == 'D', 'I', 'V', 'X'
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 1프레임과 다음 프레임 사이의 간격 설정
out = cv2.VideoWriter('infraredRaw_indoor_3.mp4', fourcc, fps, (w, h))
########################################################################

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break
    out.write(frame)

    cv2.imshow('frame', frame)
    print(frame.shape)
    # Break the loop if 'esc' is pressed
    if (cv2.waitKey(1) & 0xFF == 27):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
