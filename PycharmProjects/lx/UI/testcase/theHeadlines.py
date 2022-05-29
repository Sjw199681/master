import os, time, unittest
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from UI.common.driver import Driver
from UI.common.log import logger
from UI.common.myTest import MyTest
from UI.common.readExcel import RendExcel


"""
实现逻辑
1.导包---unittest
2.创建测试类
3.创建初始化方法-打开app，case，关闭app(清理数据)
4.测试case使用test开头
"""
re = RendExcel()


# 微头条case
class Theheadlines(MyTest):
    """
    首页点击发布，选择微头条，输入文案，点击发布
    """

    def test_run(self):
        # 获取当前方法名
        runname = self.__class__.__name__
        # 获取当前类名
        runname1 = self._testMethodName
        data = re.read(runname, runname1)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpy').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/hd').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').clear()
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys(data)
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        logger.info("发布成功")
        time.sleep(2)
        # 断言*判断是否发送成功
        page = self.driver.page_source  #获得当前页面的所有元素
        self.assertIn(data, page)

    def test_run1(self):
        # 动态休眠时间--动态休眠5s
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bpy').click()
        # time.sleep(2)
        # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/hd').click()
        # time.sleep(2)
        # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').clear()
        # time.sleep(2)
        # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bmj').send_keys("啦啦啦啦啦啦德玛西亚")
        # time.sleep(2)
        # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a96').click()
        # logger.info("发布成功")
        # time.sleep(2)


if __name__ == "__main__":
    unittest.main()
