>>> stu={'Dipali':109, 'Aish':101,'Bunny':102,'Chuck':104,'Ell':105}
>>> dir(stu)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> sizeof(stu)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sizeof(stu)
NameError: name 'sizeof' is not defined
>>> a=stu.sizeof()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=stu.sizeof()
AttributeError: 'dict' object has no attribute 'sizeof'
>>> len(stu)
5
>>> newd=stu().copy()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    newd=stu().copy()
TypeError: 'dict' object is not callable
>>> newd=dic(stu)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    newd=dic(stu)
NameError: name 'dic' is not defined
>>> newd=dict(stu)
>>> print(newd)
{'Dipali': 109, 'Aish': 101, 'Bunny': 102, 'Chuck': 104, 'Ell': 105}
>>> stu.update('deepa':107)
SyntaxError: invalid syntax
>>> stu.update({'deepa':107})
>>> print (stu)
{'Dipali': 109, 'Aish': 101, 'Bunny': 102, 'Chuck': 104, 'Ell': 105, 'deepa': 107}
>>> x=stu.get("bunny")
>>> print(x)
None
>>> 
>>> x=stu.get("Bunny")
>>> print(x)
102
>>> y=stu.items()
>>> print(y)
dict_items([('Dipali', 109), ('Aish', 101), ('Bunny', 102), ('Chuck', 104), ('Ell', 105), ('deepa', 107)])
>>> z=stu.keys()
>>> print(stu)
{'Dipali': 109, 'Aish': 101, 'Bunny': 102, 'Chuck': 104, 'Ell': 105, 'deepa': 107}
>>> print(z)
dict_keys(['Dipali', 'Aish', 'Bunny', 'Chuck', 'Ell', 'deepa'])
>>> u=stu.values()
>>> print(u)
dict_values([109, 101, 102, 104, 105, 107])
>>> a=stu.pop('Aish')
>>> print(stu)
{'Dipali': 109, 'Bunny': 102, 'Chuck': 104, 'Ell': 105, 'deepa': 107}
>>> b=stu.popitem()
>>> print(stu)
{'Dipali': 109, 'Bunny': 102, 'Chuck': 104, 'Ell': 105}
>>> c=stu.clear()
>>> print(c)
None
>>> s=setdefault.("Dipali","dips")
SyntaxError: invalid syntax
>>> s=stu.setdefault("Dipali","dips")
>>> print(s)
dips
>>> print(stu)
{'Dipali': 'dips'}
>>> tup=('key','key1','key2')
>>> stu=dict.fromkeys(tup)
>>> print(stu)
{'key': None, 'key1': None, 'key2': None}
>>> y=0
>>> stu=dict.fromkeys(tup,0)
>>> print(stu)
{'key': 0, 'key1': 0, 'key2': 0}
>>> 
