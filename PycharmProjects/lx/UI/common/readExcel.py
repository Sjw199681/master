"""
导包
1-定义一个rendexcel的类
2-定义初始化方法
    获取excel路径
    打开excel
    获取sheet页
    获取最大行数
3-定义方法read，接收一个方法名，类名
    循环获取所有数据，一行读取结果为一个列表
    判断第一列数据和第二列数据是否和目标方法一致
    是-读取第三列
    否-下一行
"""
import xlrd, os


class RendExcel:
    def __init__(self):
        # 获取excel路径
        self.excel = os.path.dirname(os.path.dirname(__file__)) + "/testdata/data.xls"
        # 打开excel
        self.readbook = xlrd.open_workbook(self.excel)
        # 获取sheet页
        self.sheet = self.readbook.sheet_by_index(0)
        # 获取最大行数
        self.nrows = self.sheet.nrows

    # 定义方法read，接收一个方法名，类名
    def read(self, runname, run2name):
        # 循环获取所有数据，一行读取结果为一个列表
        for i in range(1, self.nrows):
            list1 = self.sheet.row_values(i)
            print(list1)
            # 判断第一列数据和第二列数据是否和目标方法一致
            if list1[1] == runname and list1[2] == run2name:
                # 是 - 读取第三列
                return list1[-1]


if __name__ == '__main__':
    a = RendExcel()
    print(a.read('Theheadlines', 'test_run'))
