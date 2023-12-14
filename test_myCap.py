import cv2
import time
from FasterVideoCapture import BaseVideoCapture, FasterVideoCapture


if __name__ == "__main__":
    videoPath = [
        r"F:\researchCode\github\FasterVideoCapture\demo.mp4" for i in range(20)
    ]
    cap = FasterVideoCapture(
        videoPath=videoPath, initStep=0, interval=200, buffer_size=5
    )
    # cap=BaseVideoCapture(videoPath=videoPath,interval=400)
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
