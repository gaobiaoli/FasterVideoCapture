import cv2
class BaseVideoCapture:
    """带去畸变和间隔读取的视频播放器"""
    SKIPMODE="PERFRAME"
    def __init__(self, videoPath, initStep=0, mtx=None, dist=None) -> None:
        self.videoPath = videoPath
        self.mtx = mtx
        self.dist = dist
        self.capture = cv2.VideoCapture(videoPath)
        self.count = 0
        self.initStep = initStep
        self.initSkip(step=initStep)

    def initSkip(self, step):
        """通过set方法跳帧,适用于视频初始化时"""
        if BaseVideoCapture.SKIPMODE=="PERFRAME":
            ret=self.skip(step=step)
        else:
            ret = self._setFrame(self.count + step)
        if ret:
            self.count += step
            return True
        return False

    def skip(self, step):
        """跳过step帧"""
        for _ in range(step):
            ret = self._grab()
            if not ret:
                return False
        return True

    def _grab(self):
        """跳帧"""
        ret = self.capture.grab()
        if ret:
            self.count += 1
        return ret

    def _read(self):
        """跳帧+读帧"""
        ret, frame = self.capture.read()
        if ret:
            self.count += 1
        return ret, frame

    def _setFrame(self, index):
        """set方法跳帧"""
        ret = self.capture.set(cv2.CAP_PROP_POS_FRAMES, index)
        return ret

    def read(self, interval=1):
        """间隔interval帧读取"""
        ret = self.skip(interval - 1)
        if not ret:
            return False, None
        ret, frame = self._read()
        if ret and self.mtx is not None and self.dist is not None:
            frame = cv2.undistort(frame, self.mtx, self.dist)
        return ret, frame

    def release(self):
        self.capture.release()
        del self