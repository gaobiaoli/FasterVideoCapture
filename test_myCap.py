import cv2
import time
import numpy as np
from FasterVideoCapture import BaseVideoCapture, FasterVideoCapture


if __name__ == "__main__":
    videoPath = ["demo/demo.mp4" for _ in range(20)]
    mtx, dist = np.load("demo/undistort.npy", allow_pickle=True)
    cap = FasterVideoCapture(
        videoPath=videoPath, initStep=0, interval=200, buffer_size=5, mtx=mtx, dist=dist
    )
    # cap=BaseVideoCapture(videoPath=videoPath,interval=200,mtx=mtx,dist=dist)
    time.sleep(5)
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    while True:
        t1 = time.time()
        ret, frame = cap.read()
        if ret:
            time.sleep(1)
            cv2.imshow("video", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                cv2.destroyWindow("video")
                break
        else:
            break
        print("Frame:{}---FPS:{}".format(cap.count(), 1 / (time.time() - t1)))
