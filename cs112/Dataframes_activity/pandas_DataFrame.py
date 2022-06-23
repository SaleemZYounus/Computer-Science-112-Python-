Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: /Users/MacBook/Documents/cs112/Data_phrames_pands.py ========
Traceback (most recent call last):
  File "/Users/MacBook/Documents/cs112/Data_phrames_pands.py", line 2, in <module>
    data = p.Series([['yami' , "4'3" , "19"], ["bilal", "5'8", "18" ], ['Ian', "5'11", "18"]], index = ["yami","bilal","ian"], columns=["hight","age"])
TypeError: __init__() got an unexpected keyword argument 'columns'
>>> 
========= RESTART: /Users/MacBook/Documents/cs112/Data_phrames_pands.py ========
Traceback (most recent call last):
  File "/Users/MacBook/Documents/cs112/Data_phrames_pands.py", line 2, in <module>
    data = p.Series([["4'3" , "19"], ["5'8", "18" ], ["5'11", "18"]], index = ["yami","bilal","ian"], columns=["hight","age"])
TypeError: __init__() got an unexpected keyword argument 'columns'
>>> 
========= RESTART: /Users/MacBook/Documents/cs112/Data_phrames_pands.py ========
>>> data
      hight age
yami    4'3  19
bilal   5'8  18
ian    5'11  18
>>> 