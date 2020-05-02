import cv2
import numpy as np
 
count =0
cap = cv2.VideoCapture(0)

print(" Press c to acess camera")
c = input()

if c == 'c':
    cap.isOpened()
    
while True:
   count +=1
   ret , frame = cap.read()
   img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
   lower_range = np.array([0,10,200])
   upper_range = np.array([50,88,226])
   mask  =cv2.inRange(img, lower_range, upper_range)
            
   file_path = outpath='D:\Image_processing\output\\user'+str(count)+'.jpg'
   cv2.imwrite(file_path,mask)
   cv2.putText(frame,"Capturing...",(50,100),
               cv2.FONT_HERSHEY_PLAIN,2,(100,205,100),3)
   cv2.putText(frame,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(20,155,20),2)
   cv2.imshow('Image',frame)
        
        
   if cv2.waitKey(1)==27 or count==100:
       break
cap.release()
cv2.destroyAllWindows()
print('Samples collected')
    
    
    
    


