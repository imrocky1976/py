"""
功能：实现大顶堆构造、插入元素、删除元素、堆排序
作者：shihj
日期：2020/5/22
"""

def heap_push(heap, x):
    """
    将元素@x插入大顶堆@heap
    ---
    将元素插入二叉堆的尾部，然后依次与父元素
    比较大小，进行交换，直到满足堆条件
    """

    # x的待插入下标（堆末尾）
    i = len(heap)
    heap.append(x)

    while i > 0:

        # x父元素下标
        pi = (i - 1) // 2

        # 待插入元素大于父元素，则交换
        if x > heap[pi]:
            heap[i] = heap[pi]
            heap[pi] = x
            i = pi
        else:
            break  # 满足大顶堆，无需交换

    heap[i] = x


def heap_pop(heap):
    """
    从大顶堆@heap的堆顶弹出最大元素
    ---
    将堆顶元素与堆尾元素交换，对堆顶的新元素，
    依次比较其与子元素的大小，选取最大的子元素，
    进行交换，直到满足堆条件
    """
    if not heap:
        raise ValueError('Heap is empty.')
    # 最大元素
    res = heap[0]
    # 取出堆尾元素
    x = heap.pop()

    # 从堆顶开始
    i = 0
    while 2*i+1 < len(heap):
        # 子元素下标
        lc, rc = 2*i+1, 2*i+2
        # 选取最大的子元素
        if rc < len(heap) and heap[rc] > heap[lc]:
            lc = rc
        # 如果x已经在上层，则可以停止
        if heap[lc] <= x:
            break
        # 否则交换
        heap[i] = heap[lc]
        i = lc

    if i < len(heap):
        heap[i] = x

    return res


def heapify(arr):
    """
    从@arr列表构造大顶堆
    """
    res = []
    for x in arr:
        heap_push(res, x)

    return res


def heap_sort(heap):
    """
    对大顶堆@h降序排序
    """
    res = []
    while heap:
        res.append(heap_pop(heap))
    return res


if '__main__' == __name__:
    arr = [45, 50, 20, 35, 30, 15, 10, 40, 25]
    heap = heapify(arr)
    print(heap)
    sorted_arr = heap_sort(heap)
    print(sorted_arr)
