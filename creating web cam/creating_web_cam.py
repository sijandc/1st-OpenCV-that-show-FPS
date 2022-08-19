import cv2
import time

#for webcam
def run():
 cap = cv2.VideoCapture(0)





 while cap.isOpened():
    ret,img=cap.read()
    start = time.time()
    if not ret:
        print("Ignore")
        continue
    
    
    k=cv2.waitKey(10)
    end = time.time()
   

    totalTime=end - start
    fps = 1/totalTime
    print("FPS: ",fps)
    cv2.putText(img,f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
    cv2.imshow('sijan cam',img)
    k=cv2.waitKey(5)
    if k ==27:
        break;
 print(start)
 print(end)

 cap.release()
 return run

 
run()