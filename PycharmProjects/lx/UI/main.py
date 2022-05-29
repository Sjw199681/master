import os, time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


# 获取屏幕尺寸
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 上滑
def swiPe(driver):
    x1 = getSize(driver)[0] * 0.5
    y1 = getSize(driver)[1] * 0.75
    y2 = getSize(driver)[1] * 0.25
    driver.swipe(x1, y1, x1, y2, 1000)


# 下滑动
def glide(driver):
    x1=getSize(driver)[0]*0.3
    y1=getSize(driver)[1]*0.2
    y2=getSize(driver)[1]*0.8
    driver.swipe(x1,y1,x1,y2,1000)

#左滑动
def left_slide(driver):
    x1 = getSize(driver)[0] * 0.25
    x2 = getSize(driver)[0] * 0.75
    y1 = getSize(driver)[1] * 0.5
    driver.swipe(x1, y1, x2, y1, 1000)


#右滑动
def right_slide(driver):
    x1 = getSize(driver)[0] * 0.75
    x2 = getSize(driver)[0] * 0.25
    y1 = getSize(driver)[1] * 0.5
    driver.swipe(x1, y1, x2, y1, 1000)


def starUP():
    desired_caps = {
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
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print("完成启动")
    time.sleep(6)
    # 返回text文本
    # print(driver.find_element(By.ID,'com.ss.android.article.news:id/title').get_attribute("text"))
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/bpy').click()
    # time.sleep(2)
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/hd').click()
    # time.sleep(2)
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').clear()
    # time.sleep(2)
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys("啦啦啦啦啦啦德玛西亚")
    # time.sleep(2)
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
    # print("发布成功")
    # time.sleep(2)
    # 获得当前页面的所有元素
    result = driver.page_source
    assert '啦啦啦啦啦啦德玛西亚' in result
    print("断言成功")
    # 点击指定坐标
    driver.tap([(200,300)],2)
    action = TouchAction(driver)
    action.press(x=220, y=700).move_to(x=840, y=700).move_to(x=220, y=1530).move_to(x=840, y=1530).release().perform()

    # 获取屏幕尺寸
    getSize(driver)

    # 上滑
    swiPe(driver)
    time.sleep(2)
    #下滑
    glide(driver)
    time.sleep(2)
    #左滑动
    left_slide(driver)
    time.sleep(2)
    #右滑动
    right_slide(driver)


if __name__ == '__main__':
    starUP()
