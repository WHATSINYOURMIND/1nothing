Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1="I live my country"
>>> s1
'I live my country'
>>> s1.isalnum()
False
>>> s2="vidyalankar"
>>> s2.isalpha()
True
>>> s2.isdigit()
False
>>> s3='1234'
>>> s3.isnumeric()
True
>>> s2.isupper()
False
>>> s2.islower()
True
>>> s2.isspace()
False
>>> s2.upper()
'VIDYALANKAR'
>>> print(s2)
vidyalankar
>>> s2.lower()
'vidyalankar'
>>> s1="I love my country"
>>> s1
'I love my country'
>>> s1.capitalize()
'I love my country'
>>> s2.calitalize()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s2.calitalize()
AttributeError: 'str' object has no attribute 'calitalize'
>>> s2.capitalize()
'Vidyalankar'
>>> s1.title()
'I Love My Country'
>>> s1.replace('country','family')
'I love my family'
>>> s1.split()
['I', 'love', 'my', 'country']
>>> s2="ABC,PQR XYZ"
>>> s2.split(',')
['ABC', 'PQR XYZ']
>>> s1
'I love my country'
>>> s1.swapcase()
'i LOVE MY COUNTRY'
>>> len(s1)
17
>>> s1.find("country")
10
>>> s1.index("country")
10
>>> s3="   Vidyalankar   "
>>> s3
'   Vidyalankar   '
>>> s3.strip()
'Vidyalankar'
>>> s3.lstrip()
'Vidyalankar   '
>>> s3.rstrip()
'   Vidyalankar'
>>> 