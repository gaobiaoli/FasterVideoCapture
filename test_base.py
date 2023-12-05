import cv2
import time
from FasterVideoCapture import BaseVideoCapture


if __name__=="__main__":
    videoPath="demo.mp4"
    cap=BaseVideoCapture(videoPath=videoPath)
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    while True:
        t1=time.time()
        ret,frame=cap.read()
        if ret:
            cv2.imshow("video", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                cv2.destroyWindow("video")
                break
        print("Frame:{}---FPS:{}".format(cap.count,1/(time.time()-t1)))
        
