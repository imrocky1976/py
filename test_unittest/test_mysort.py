import unittest
import mysort

# 编写子类继承 unittest.TestCase
class TestSort(unittest.TestCase):

   # 以 test 开头的函数将会被测试
   def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        mysort.sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])

if __name__ == '__main__':
    ## 如果在 Jupyter 下，请用如下方式运行单元测试
    ## unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    ## 如果是命令行下运行，则：
    unittest.main()
    
## 输出
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.002s
#
#OK
