Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[10,20.5,"ABC"]
>>> l1
[10, 20.5, 'ABC']
>>> l1[0]
10
>>> l1[1]=30.7
>>> l1
[10, 30.7, 'ABC']
>>> l2=[10,10,20]
>>> l2
[10, 10, 20]
>>> t1=(10,20,30,10,"ABC")
>>> t1
(10, 20, 30, 10, 'ABC')
>>> t1[0]
10
>>> t1[1]=100
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t1[1]=100
TypeError: 'tuple' object does not support item assignment
>>> t1
(10, 20, 30, 10, 'ABC')
>>> s1={10,20,30,"ABC",20}
>>> s1
{'ABC', 10, 20, 30}
>>> s1[0]=100
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1[0]=100
TypeError: 'set' object does not support item assignment
>>> d1={10:"AAA",20:"BBB","CCC":30}
>>> d1
{10: 'AAA', 20: 'BBB', 'CCC': 30}
>>> d1[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d1[0]
KeyError: 0
>>> d1[10]
'AAA'
>>> d1[10]="XYZ"
>>> d1
{10: 'XYZ', 20: 'BBB', 'CCC': 30}
>>> 