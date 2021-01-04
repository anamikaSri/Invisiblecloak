import cv2
import numpy as np

cap=cv2.VideoCapture(0)
background=cv2.imread('image.jpg')

while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv , lower_red , upper_red)
    
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
        mask1 = mask1 + mask2 #OR
        mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
        
        mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)
        
        mask2 = cv2.bitwise_not(mask1)
    
        res1 = cv2.bitwise_and(background, background, mask=mask1)
        res2 = cv2.bitwise_and(frame,frame, mask=mask2)
    
        final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
        cv2.imshow('image.jpg' , final_output)
        if cv2.waitKey(5)==ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()
