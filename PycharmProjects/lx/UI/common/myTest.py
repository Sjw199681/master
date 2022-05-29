import unittest
from UI.common.driver import Driver

"""
抽取testcase中的公共方法，定义到父类中，减少代码量，方便维护
1.倒包
"""


class MyTest(unittest.TestCase):
    # 所有case执行完毕之后启动
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().starUP()

    # 隔离每条case之间的数据依赖
    def setUp(self):
        self.driver.launch_app()

    # 初始化方法-每条case执行完毕后关闭app
    # def tearDown(self):
    #     self.driver.close()

    # 隔离每条case之间的数据依赖-不需要每次都关闭
    def tearDown(self):
        self.driver.close_app()

    # 所有case执行完毕之后关闭
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
