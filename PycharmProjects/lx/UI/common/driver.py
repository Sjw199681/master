# 导包
import os, time
from appium import webdriver


# 创建初始化方法
class Driver():
    def __init__(self):
        # 配置启动参数
        self.desired_caps = {
            "platformName": "Android",  # 操作系统
            "deviceName": "127.0.0.1:62001",  # 设备 ID adb devices
            "platformVersion": "7.1.2",  # 设备版本号
            "appPackage": "com.ss.android.article.news",  # app 包名
            "appActivity": "com.ss.android.article.news.activity.MainActivity",  # app 启动时主 Activity
            'noReset': True,  # 是否保留 session 信息，可以避免重新登录
            'autoLaunch Appium': True,
            'automationName': 'UiAutomator1',
            'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
            'resetKeyboard': False  # 将键盘给隐藏起来
        }

    # 创建实例方法--创建driver,方便外部调用
    def starUP(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        print("完成启动")
        time.sleep(6)
        return driver



if __name__ == '__main__':
    pass
