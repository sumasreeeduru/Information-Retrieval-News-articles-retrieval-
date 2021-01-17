Project - IR system for news articles




Trie is used for inserting words and AVL Tree for creating posting list
Time complexity of inverted index is O(logn)
Space complexity of inverted index is O(n) 


Crawler.py consists of the code for crawling a web page and extracting the urls present in it
scraper.py consists of the code for parsing through the text in web page 
index_rank.py consists of the code for creating posting list (then ouput.txt is produced) and also giving score for the documents based on vector space
model and ranking top 10 documents

Modules to install:
pip install beautiful soup
pip install stop_words

Steps to run:
1. run Crawler.py ( python Crawler.py "url") (url format: "http://en.wikipedia.org/wiki/news") (NOTE : it should be http not https) ---> It creates file.txt
2. run scraper.py ( python scraper.py) --> It creates folder "dataset" which contains all the documents 
3. run index_rank.py --- > It creates "output.txt" which has inverted index
4. Then top 10 document ids are printed
