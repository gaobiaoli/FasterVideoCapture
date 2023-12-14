import time
import cv2

if __name__ == "__main__":
    cap = cv2.VideoCapture("./demo.mp4")
    interval = 200
    time.sleep(3)
    cv2.namedWindow("video", cv2.WINDOW_NORMAL)
    count = 0
    t1 = time.time()
    while True:

        ret, frame = cap.read()
        count += 1
        if ret:
            if count % interval != 0:
                continue

            time.sleep(1)
            cv2.imshow("video", frame)
            k = cv2.waitKey(1) & 0xFF
            print("Frame:{}---FPS:{}".format(count, 1 / (time.time() - t1)))
            t1 = time.time()
            if k == 27:
                cv2.destroyWindow("video")
                break
        else:
            break
