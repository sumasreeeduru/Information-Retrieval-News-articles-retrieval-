import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
# Make a request


hand=open("file.txt","r")
num=1
print(hand)
for j in hand:
    
    page=urllib.request.urlopen(j).read()
    soup=BeautifulSoup(page,'html.parser')
    page_body=soup.body
    p=page_body.text
    
    for i in page_body.text:
        if ord(i)<65 or ord(i)>122:
            p=p.replace(i,' ')
        if ord(i)>90 and ord(i)<97:
            p=p.replace(i,' ')
    
    file1 = open("documents/%d.txt"%(num),"w")
    num=num+1
    file1.write(p)
