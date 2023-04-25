#Read source code of any web page
import urllib.request
f1=urllib.request.urlopen("https://www.python.org")
print(f1.read())
