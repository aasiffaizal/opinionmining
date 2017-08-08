from bs4 import BeautifulSoup
import requests

def scrap(keyword):    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    url="https://www.reddit.com/search?q="+keyword
    r  = requests.get(url,headers=headers)
    data=r.text
    topic_links=[]
    soup = BeautifulSoup(data, 'html.parser')
    
    

    headertag=soup.find_all("header", {"class":"search-result-header"})

    for headers in headertag:
        linktag=headers.find_all("a",{"class":"search-title may-blank"})
        for link in linktag:
            newl=link.get('href')
            newl=str(newl)
            topic_links.append(newl)
    for divs in soup.find_all("div", attrs={'class':' search-result search-result-subreddit '}):
        linktag=divs.find_all("a",{"class":"search-title may-blank"})
        for link in linktag:
            rem=link.get('href')
        for i in topic_links:
            if i in rem:
                topic_links.remove(i)

    content_div=soup.find_all("div", {"class":"search-result-group"})
    for contents in content_div:
        span_tag=contents.find_all("span",{"class":"nextprev"})
        for spans in span_tag:
            a_tag=spans.find_all("a")
            for a in a_tag:
                slink=a.get('href')
    slink=str(slink)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    r  = requests.get(slink,headers=headers)
    data=r.text
    soup = BeautifulSoup(data, 'html.parser')
    headertag=soup.find_all("header", {"class":"search-result-header"})

    for headers in headertag:
        linktag=headers.find_all("a",{"class":"search-title may-blank"})
        for link in linktag:
            newl=link.get('href')
            newl=str(newl)
            topic_links.append(newl)
    for divs in soup.find_all("div", attrs={'class':' search-result search-result-subreddit '}):
        linktag=divs.find_all("a",{"class":"search-title may-blank"})
        for link in linktag:
            rem=link.get('href')
        for i in topic_links:
            if i in rem:
                topic_links.remove(i)
    total_comments=[]
    print topic_links
    count=0
    flag=0
    for i in topic_links:
        if flag == 1:
            break
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
        url=i+"?limit=500"
        r  = requests.get(url,headers=headers)
        data=r.text
        soup = BeautifulSoup(data, 'html.parser')
        l=[]
        divTag = soup.find_all("div", {"class": "commentarea"})
        for relcomm in divTag:
            if flag == 1:
                break
            comments=relcomm.find_all("div", attrs={'class':'md'})
            for divs in comments:
                count+=1
                if count > 5000:
                    flag=1
                    break
                l.append(divs.get_text())


        for divs in soup.find_all("div", attrs={'class':'titlebox'}):
            rem=divs.get_text()
        for i in l:
            if i in rem:
                l.remove(i)
        for i in l:
            total_comments.append(i)
            print i
    return total_comments


        










