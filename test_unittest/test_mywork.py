import mywork
import unittest
from unittest.mock import patch

class A(unittest.TestCase):

    def test_preprocess(self):
        arr = 1
        w = mywork.Work()
        w.preprocess(arr)
        self.assertTrue(True)
        
    @patch("mywork.Work.preprocess")
    def test_sort(self, mock_preprocess):
        arr = 1
        mock_preprocess.return_value = {"result": "success", "reason":"null"}
        w = mywork.Work()
        # 假定sort中调用preprocess
        # 根据mock_preprocess返回值测试sort
        w.sort(arr)
        self.assertTrue(True)
        
    def test_postprocess(self):
        arr = 1
        w = mywork.Work()
        w.postprocess(arr)
        self.assertTrue(True)
        
    @patch('mywork.Work.preprocess')
    @patch('mywork.Work.sort')
    @patch('mywork.Work.postprocess')
    def test_work(self,mock_post_process, mock_sort, mock_preprocess):
        w = mywork.Work()
        w.work()
        self.assertTrue(mock_post_process.called)
        self.assertTrue(mock_sort.called)
        self.assertTrue(mock_preprocess.called)

