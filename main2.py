import cv2
import numpy as np
 
 
frame = cv2.imread("/home/juno/Perspective Transformation/images/download.png")



left_top = [274,783]
right_top = [650,783]
left_bottom = [14,986]
right_bottom = [709,988]
 
w = int(np.linalg.norm(np.array(right_top) - np.array(left_top)))
h = int(np.linalg.norm(np.array(left_bottom) - np.array(left_top)))
print(f"{w} x {h}")
 
# Coordinates that you want to Perspective Transform
pts1 = np.float32([left_top,right_top,left_bottom,right_bottom])
# Size of the Transformed Image
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
 
print(f"pst1: {pts1}")
print(f"pst2: {pts2}")
 
# for val in pts1:
#     cv2.circle(frame,(val[0],val[1]),5,(0,0,255),-1)
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(frame,M,(int(w),int(h)))
 
cv2.imshow("paper", frame)
cv2.imshow("dst", dst)
 
cv2.imwrite("data.jpg", frame)
cv2.imwrite("data1.jpg", dst)
cv2.waitKey()
cv2.destroyAllWindows()