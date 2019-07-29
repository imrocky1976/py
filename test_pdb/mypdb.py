def func():
    print('enter func()')

a = 1
b = 2
import pdb
pdb.set_trace()
func()
c = 3
print(a + b + c)

"""
# pdb
> /Users/jingxiao/test.py(9)<module>()
-> func()
(pdb) s
--Call--
> /Users/jingxiao/test.py(1)func()
-> def func():
(Pdb) l
  1  ->	def func():
  2  		print('enter func()')
  3
  4
  5  	a = 1
  6  	b = 2
  7  	import pdb
  8  	pdb.set_trace()
  9  	func()
 10  	c = 3
 11  	print(a + b + c)

(Pdb) n
> /Users/jingxiao/test.py(2)func()
-> print('enter func()')
(Pdb) n
enter func()
--Return--
> /Users/jingxiao/test.py(2)func()->None
-> print('enter func()')

(Pdb) n
> /Users/jingxiao/test.py(10)<module>()
-> c = 3
"""