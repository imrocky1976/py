from search_engine_base import SearchEngineBase, main
import re
import heapq
import functools

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    """
    根据 query_words 拿到所有的倒序索引，如果拿不到，就表示有的 query word 不存在于任何文章中，
    直接返回空；拿到之后，运行一个“合并 K 个有序数组”的算法，从中拿到我们想要的 ID，并返回。
    
    这里用到的算法并不是最优的，最优的写法需要用最小堆来存储 index。这是一道有名的 leetcode hard 题，有兴趣请参考：
    https://blog.csdn.net/qqxx6661/article/details/77814794
    """
    @functools.lru_cache(maxsize=32, typed=False)
    def search(self, query):
        print("begin search")
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()
        for query_word in query_words:
            query_words_index.append(0)
        
        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        
        inverted_index_lists = []
        for query_word in query_words:
            #print(self.inverted_index[query_word])
            inverted_index_lists.append(self.inverted_index[query_word])
        return self.merge_k_ordered_lists(inverted_index_lists)
        """
        result = []
        while True:
            
            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []
            
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                
                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue
            
            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1
        """
    @staticmethod
    def merge_k_ordered_lists(lists):
        dummy = []
        head = []
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(head, (lists[idx][0], idx))
                lists[idx] = lists[idx][1:]
        while head:
            if all(x[0] == head[0][0] for x in head):
                dummy.append(head[0][0])
            _, idx = heapq.heappop(head)
            if lists[idx]:
                heapq.heappush(head, (lists[idx][0], idx))
                lists[idx] = lists[idx][1:]
            else:
                break
        return dummy

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)

if '__main__' == __name__:
    search_engine = BOWInvertedIndexEngine()
    main(search_engine)
