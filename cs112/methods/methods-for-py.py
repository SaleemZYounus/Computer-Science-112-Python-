Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fri='clas no fri wish'
>>> dir(fri)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fri.count("s")
2
>>> fri.find(" ")
4
>>> fri.isalpha()
False
>>> alpha="efacbd"
>>> alpha.isalpha()
True
>>> fri.join('^_^')
'^clas no fri wish_clas no fri wish^'
>>> fri.join('1. 2. 3.')
'1clas no fri wish.clas no fri wish clas no fri wish2clas no fri wish.clas no fri wish clas no fri wish3clas no fri wish.'
>>> fri.join(---)
SyntaxError: invalid syntax
>>> fri.join('---')
'-clas no fri wish-clas no fri wish-'
>>> fri.upper()
'CLAS NO FRI WISH'
>>> fri.upper("yes")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fri.upper("yes")
TypeError: str.upper() takes no arguments (1 given)
>>> fri.sort()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fri.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> fri.title()
'Clas No Fri Wish'
>>> fri.split(" ")
['clas', 'no', 'fri', 'wish']
>>> fri.split()
['clas', 'no', 'fri', 'wish']
>>> list(friday)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(friday)
NameError: name 'friday' is not defined
>>> list(fri)
['c', 'l', 'a', 's', ' ', 'n', 'o', ' ', 'f', 'r', 'i', ' ', 'w', 'i', 's', 'h']
>>> 