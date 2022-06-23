Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=[1,2,3,4,5]
>>> sqr = list(map(squares, num))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sqr = list(map(squares, num))
NameError: name 'squares' is not defined
>>> def
SyntaxError: invalid syntax
>>> def sqrs(num):
	return num**2

>>> sqr = list(map(squares, num))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sqr = list(map(squares, num))
NameError: name 'squares' is not defined
>>> sqr = list(map(sqrs, num))
>>> sqr
[1, 4, 9, 16, 25]
>>> pi = ['1.0','2.1']
>>> float(pi)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(pi)
TypeError: float() argument must be a string or a number, not 'list'
>>> 