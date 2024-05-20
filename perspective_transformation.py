import cv2
import numpy as np
 
win_name = "scanning"
img_time = "11.77"
frame = cv2.imread("/Users/juno/Perspective_Transformation/0416_13km/frame_" + img_time + ".jpg")
draw = frame.copy()

pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)


def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        # 좌표에 초록색 동그라미 표시
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        # 마우스 좌표 저장
        pts[pts_cnt] = [x, y]
        pts_cnt += 1
        if pts_cnt == 4:

            # topLeft = pts[0]
            bottomRight = pts[2]
            topRight = pts[3]
            bottomLeft = pts[1]

            topLeft = [385. , 563.]
            # bottomRight = [1212. , 979.]
            # topRight = [1690. , 768.]
            # bottomLeft = [120. , 592.]

            print("topLeft =", topLeft)
            print("bottomRight =", bottomRight)
            print("topRight =", topRight)
            print("bottomLeft =", bottomLeft)

            w = int(np.linalg.norm(np.array(topRight) - np.array(topLeft)))
            h = int(np.linalg.norm(np.array(bottomLeft) - np.array(topLeft)))
            print(f"{w} x {h}")
            
            # Coordinates that you want to Perspective Transform
            pts1 = np.float32([topLeft,topRight,bottomLeft,bottomRight])
            # Size of the Transformed Image
            pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
            
            M = cv2.getPerspectiveTransform(pts1,pts2)
            dst = cv2.warpPerspective(frame,M,(int(w),int(h)))
            
            cv2.imwrite("./transformed_images/" + img_time + ".jpg", dst)
            cv2.imshow("dst", dst)
            
            

cv2.imshow(win_name, frame)
cv2.setMouseCallback(win_name, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()