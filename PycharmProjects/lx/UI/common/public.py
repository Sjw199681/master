from UI.common.driver import Driver
from appium import webdriver


class PuBlic:
    def __init__(self, driver):
        self.driver = driver

    # 获取屏幕尺寸
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

     # 上滑
    def swiPe(self):
        x1 = self.getSize()[0] * 0.5
        y1 = self.getSize()[1] * 0.75
        y2 = self.getSize()[1] * 0.25
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 下滑动
    def glide(self):
        x1 = self.getSize()[0] * 0.3
        y1 = self.getSize()[1] * 0.2
        y2 = self.getSize()[1] * 0.8
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 左滑动
    def left_slide(self):
        x1 = self.getSize()[0] * 0.25
        x2 = self.getSize()[0] * 0.75
        y1 = self.getSize()[1] * 0.5
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 右滑动
    def right_slide(self):
        x1 = self.getSize()[0] * 0.75
        x2 = self.getSize()[0] * 0.25
        y1 = self.getSize()[1] * 0.5
        self.driver.swipe(x1, y1, x2, y1, 1000)


if __name__ == '__main__':
    driver = Driver().starUP()
    PuBlic(driver).right_slide()