a = 10
b="2"
try:
    res = a + b 
except TypeError:
    try:
        res = a + int(b)
        print(res)
    except Exception as e:
        print(a+float(b))