'7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引'
# "先用空格进行分割，得到一个列表，列表内由每个单词组成，然后依次取列表内的单词用&进行继续切片，"
# "切完判断长度，如果长度大于1证明被切了，然后拼接这个大于1的，打印他，就出来了