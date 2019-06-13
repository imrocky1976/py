import numpy
import  time
l=[]
sl=set()
dl=dict()
#LEN = 100000
LEN = 400
r=numpy.random.randint(0,10000000,LEN)
for i in range(0,LEN):
    l.append(r[i])
    sl.add(r[i])
    dl.setdefault(r[i],1)
#生成3种数据结构供查找，常规的list,集合sl,字典dl.里面的元素都是随机生成的，为什么要随机生成元素？这是防止某些结构对有序数据的偏向导致测试效果不客观。

start=time.clock()
for i in range(LEN):
    t=i in sl
end=time.clock()
print("set:",end-start)
#计算通过set来查找的效率
start=time.clock()
for i in range(LEN):
    t=i in dl
end=time.clock()
print("dict:",end-start)
#计算通过dict的效率
start=time.clock()
for i in range(LEN):
    t=i in l
end=time.clock()
print("list:",end-start)
#计算通过list的效率
