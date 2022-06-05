#download pages from the net
import requests
#if you want to download you need to pass the link of download here.
#that link will return an object
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
#this object has a status code, which if is 200, means everything is okay
print(res.status_code)
#all the text is in the object. so to see that text u need this .text 
print(len(res.text))

print(res.text[:500])
#this below is used if you want to see if the download occur or not
print(res.raise_for_status())
