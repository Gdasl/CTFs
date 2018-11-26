import requests
import re

r = re.compile('<a href="(.*?)" style="')
url = 'http://fun.ritsec.club:8007'
mastArr = []
visited = []

def crawl(url):
    resp = requests.get(url).text
    if 'flag' in resp:
        print resp
        
    url = 'http://fun.ritsec.club:8007'
    arr = r.findall(resp)
    if len(arr) == 0:
        print "end link found"
        mastArr.append(resp)
    else:
        
        print "%d links found"%len(arr)
        for item in arr:
            if item not in visited:
                print url + '/%s'%item
                visited.append(item)
                crawl(url + '/%s'%item)
