import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라 안됨1')
    exit()

# 웹 캠을 출력
while 1:
    # 카메라에서 프레임을 읽기
    ret, frame = cap.read()
    
    if not ret:
        print('카메라 안됨2')
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.imshow("frame gray", frame_gray)

    # 종료키 입력
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
