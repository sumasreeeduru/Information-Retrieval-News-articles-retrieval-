import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
import re 
import sys

#function
def crawler(soup,urls,visited,url):
        for tag in soup.find_all('a', href= True):
                colon = ":" 
                hashtag = "#"
                main = "Main_Page"
                wiki_eng = "http://en.wikipedia.org/wiki/"
                
                if colon not in tag['href'] and hashtag not in tag['href']:
                        tag['href'] = urllib.parse.urljoin(url,tag['href'])
                        if(str(tag['href']).startswith(wiki_eng)) and str(tag['href']).find(main) == -1:
                            if (tag['href'] not in urls and tag['href'] not in visited):
                                urls.append(tag['href'])
                                visited.append(tag['href'])
                else: 
                    continue
        time.sleep(1)
        

#main 
if len(sys.argv) > 1: 
        url= sys.argv[1]
else:
        exit(0)
urls = [url] #queue of urls to scrape
visited = [] #queue of visited urls 
canonical_links = set() #set of canonical links
nodes_curr_level = 1 
nodes_next_level = 0 
depth = 0
visited_links = 0
c=0     
while len(urls) > 0:
   
    
    if depth == 3: 
            exit(0)
    
    while nodes_curr_level != 0:
        
        htmltext = urllib.request.urlopen(urls[0]).read()
        soup = BeautifulSoup(htmltext)
        nodes_curr_level -= 1
        urls.pop(0)
        if len(sys.argv) == 3:
            if soup.find_all(text=re.compile(sys.argv[2], re.IGNORECASE)) == []:
                continue
        links = soup.find('link', {"rel":"canonical"})
        link1 = links['href']
        if link1 in canonical_links:continue
        canonical_links.add(link1)
        visited_links += 1
        # Write the links to a file
        f = open("file.txt", 'w')
        for link in canonical_links:
            
            f.write("%s\n" % link)
            

        f.close()
        crawler(soup,urls,visited,url)
        
    visited_links = 0
    nodes_next_level = len(urls)
    if nodes_curr_level == 0:
        nodes_curr_level = nodes_next_level
        nodes_next_level = 0
        depth += 1
