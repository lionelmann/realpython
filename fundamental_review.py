Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 1, in <module>
    from capitals import capitals_dict
  File "/Users/lmann/Sites/realpython/capitals.py", line 6
    "Ontario": "Toronto",
             ^
SyntaxError: invalid syntax
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = random.choice(capital_dict.keys)
NameError: name 'capital_dict' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = random.choice(capitals_dict.keys)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 253, in choice
    i = self._randbelow(len(seq))
TypeError: object of type 'builtin_function_or_method' has no len()
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = random.choice(capitals_dict.keys())
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
TypeError: 'dict_keys' object does not support indexing
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = random.choice(capitats_dict)
NameError: name 'capitats_dict' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = random.choice(capitals_dict)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
KeyError: 5
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = choice(capitals_dict)
NameError: name 'choice' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 4, in <module>
    print(random.choice(capitals_dict.keys()))
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
TypeError: 'dict_keys' object does not support indexing
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Manitoba', 'Saskatchewan', 'Quebec', 'British Columbia', 'Ontario', 'Alberta'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 4, in <module>
    print(capitals_dict.item())
AttributeError: 'dict' object has no attribute 'item'
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_items([('Saskatchewan', 'Regina'), ('Ontario', 'Toronto'), ('Alberta', 'Edmonton'), ('Manitoba', 'Winnipeg'), ('British Columbia', 'Vancouver'), ('Quebec', 'Montreal')])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
dict_items([('Quebec', 'Montreal'), ('Ontario', 'Toronto'), ('Saskatchewan', 'Regina'), ('Alberta', 'Edmonton'), ('British Columbia', 'Vancouver'), ('Manitoba', 'Winnipeg')])
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    print(capitals_dict.items())
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Quebec', 'Saskatchewan', 'Manitoba', 'Ontario', 'British Columbia', 'Alberta'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    print(random.choice(capitals_dict.keys()))
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
TypeError: 'dict_keys' object does not support indexing
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Alberta', 'Ontario', 'British Columbia', 'Manitoba', 'Quebec', 'Saskatchewan'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Alberta', 'Saskatchewan', 'British Columbia', 'Ontario', 'Quebec', 'Manitoba'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(random.choice(capital))
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
TypeError: 'dict_keys' object does not support indexing
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(random.choice(capital.keys()))
AttributeError: 'dict_keys' object has no attribute 'keys'
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(random.choice(capital.items()))
AttributeError: 'dict_keys' object has no attribute 'items'
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(random.choice(capital.item()))
AttributeError: 'dict_keys' object has no attribute 'item'
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Saskatchewan', 'Ontario', 'British Columbia', 'Quebec', 'Manitoba', 'Alberta'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_items([('Saskatchewan', 'Regina'), ('Manitoba', 'Winnipeg'), ('British Columbia', 'Vancouver'), ('Quebec', 'Montreal'), ('Alberta', 'Edmonton'), ('Ontario', 'Toronto')])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Ontario', 'Manitoba'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_values(['Montreal', 'Winnipeg', 'Regina', 'Toronto', 'Edmonton', 'Vancouver'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    provinces = capitabls_dict.keys()
NameError: name 'capitabls_dict' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 7, in <module>
    print(capital)
NameError: name 'capital' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_values(['Winnipeg', 'Montreal', 'Toronto', 'Vancouver', 'Regina', 'Edmonton'])
dict_keys(['Manitoba', 'Quebec', 'Ontario', 'British Columbia', 'Saskatchewan', 'Alberta'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
dict_keys(['Manitoba', 'British Columbia', 'Saskatchewan', 'Quebec', 'Alberta', 'Ontario'])
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
{'British Columbia': 'Vancouver', 'Alberta': 'Edmonton', 'Ontario': 'Toronto', 'Manitoba': 'Winnipeg', 'Quebec': 'Montreal', 'Saskatchewan': 'Regina'}
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}
{'Manitoba': 'Winnipeg', 'Alberta': 'Edmonton', 'British Columbia': 'Vancouver', 'Saskatchewan': 'Regina', 'Quebec': 'Montreal', 'Ontario': 'Toronto'}Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 10, in <module>
    print(capital)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 9, in <module>
    capital = random.choice(capitals_dict)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/random.py", line 256, in choice
    return seq[i]
KeyError: 4
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 9, in <module>
    capital = capitals_dict[capital]
KeyError: ''
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 10, in <module>
    capital = capitals_dict[capital]
KeyError: ''
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Manitoba Winnipeg
Quebec Montreal
Ontario Toronto
British Columbia Vancouver
Alberta Edmonton
Saskatchewan Regina
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(capital, capitals_dict[capital])
NameError: name 'capital' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Quebec
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Ontario
Toronto
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = capitals_dict[state]
NameError: name 'state' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 5, in <module>
    capital = capitals_dict[state]
NameError: name 'state' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Manitoba
Winnipeg
What is the capital of Winnipeg?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
British Columbia
Vancouver
What is the capital of Vancouver?exit
Goodbye
What is the capital of Vancouver?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Manitoba
Winnipeg
What is the capital of Winnipeg?exit
Goodbye
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Saskatchewan
Regina
What is the capital of Regina?exit
Goodbye
What is the capital of Regina?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Ontario
Toronto
What is the capital of Toronto?exit
Goodbye
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Saskatchewan
Regina
What is the capital of Regina?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Alberta
Edmonton
What is the capital of Alberta?Edmonton
Correct
What is the capital of Alberta?asdf
What is the capital of Alberta?asdf
What is the capital of Alberta?asdf
What is the capital of Alberta?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Ontario
Toronto
What is the capital of Ontario?EXIT
What is the capital of Ontario?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Alberta
Edmonton
What is the capital of Alberta?EXIT
Goodbye
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Quebec
Montreal
What is the capital of Quebec?montreal
Correct
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Quebec
Montreal
What is the capital of Quebec?asdf
What is the capital of Quebec?MONTREAL
Correct
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Saskatchewan
Regina
What is the capital of Saskatchewan?Regina
Correct
The capital of Saskatchewan is Regina
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Saskatchewan Regina
What is the capital of Saskatchewan?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 21, in <module>
    captial_game(province, capital)
NameError: name 'captial_game' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
What is the capital of Quebec?asdf
What is the capital of Quebec?asdfkh
What is the capital of Quebec?MONTREAL
Correct
The capital of Quebec is Montreal
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 6, in <module>
    print(province, capital)
NameError: name 'province' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Quebec Montreal
What is the capital of Quebec?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 16, in <module>
    capital  = capitals_dict[province]
TypeError: unhashable type: 'list'
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Traceback (most recent call last):
  File "/Users/lmann/Sites/realpython/capital_city_loop.py", line 15, in <module>
    province = choice(list(capitals_dict.keys()))
NameError: name 'choice' is not defined
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
British Columbia Vancouver
What is the capital of British Columbia?fad
What is the capital of British Columbia?
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Manitoba Winnipeg
What is the capital of Manitoba?lj
What is the capital of Manitoba?Winnipeg
Correct
The capital of Manitoba is Winnipeg
>>> 
======== RESTART: /Users/lmann/Sites/realpython/capital_city_loop.py ========
Manitoba Winnipeg
What is the capital of Manitoba?
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  False
one:   True
two:   True
three: True
four:  True
five:  True
five:  True
six:   True
seven: True

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  False
one:   False
two:   False
three: True
four:  True
five:  False
five:  False
six:   False
seven: False

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   False
two:   False
three: True
four:  True
five:  False
five:  False
six:   False
seven: False

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   False
three: True
four:  True
five:  False
five:  False
six:   False
seven: False

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   True
three: True
four:  True
five:  False
five:  False
six:   False
seven: False

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   True
three: True
four:  True
five:  False
five:  False
six:   False
seven: True

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   True
three: True
four:  True
five:  False
five:  False
six:   True
seven: True

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   True
three: True
four:  True
five:  False
five:  True
six:   True
seven: True

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
========== RESTART: /Users/lmann/Sites/realpython/cats_with_hats.py ==========

# -- part 1 -- #
zero:  True
one:   True
two:   True
three: True
four:  True
five:  True
five:  True
six:   True
seven: True

# -- part 2 -- #
True
True
True
True
True
True
True
True
>>> 
