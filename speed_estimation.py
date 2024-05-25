import cv2
img_time = "12.93" # s
img_path = "./transformed_images/"+ img_time +".jpg"
print(img_path)
win_name = "length_estimation"

frame = cv2.imread(img_path)
width = frame.shape[1]

time_start = 10.67

full_length = 12 # m
estimated_length = 0 # m

def onMouse(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, frame)
        estimated_length = (x/width)*full_length # m
        estimated_velocity = (estimated_length/1000.0) / ((float(img_time)-time_start)/3600.0) # km/h
        print("length : %.1f [m]" % estimated_length)
        print("velocity : %.1f [km/h]" % estimated_velocity)
        


cv2.imshow(win_name, frame)
cv2.setMouseCallback(win_name, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()