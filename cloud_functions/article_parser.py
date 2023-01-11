import requests # Allows us to get the actual HTML page
from bs4 import BeautifulSoup, NavigableString # Spider / WebCrawler

def filterFunct(arrayOfLinks, addedUrl):
    setOfLinks = set()
    for link in arrayOfLinks:
        if (len(link) < 2):
            continue
        if link == "None" or link[0:4] == "mail":
            continue
        elif link[0:5] == "//www":
            setOfLinks.add("https:" + link)
        elif link[0:4] == "http":
            setOfLinks.add(link)
        else:
            setOfLinks.add(addedUrl + link)
    return setOfLinks

def initialParser(url):
    req = requests.get(url) # Get HTML Page
    htmlPage = str(req.content, "utf-8") # Stringify HTML page
    parsableHTML = BeautifulSoup(htmlPage, features="html.parser") # Make the HTML page a Soup Class
    # Time to get all the links from the HTML page
    arrayOfLinks = []
    for link in parsableHTML.find_all('a'):
        arrayOfLinks.append(link.get('href'))
    setOfLinks = filterFunct(arrayOfLinks, url)
    listOfLinks = list(setOfLinks)
    return listOfLinks

def articleParser(url):
    # Second Webcrawler
    req = requests.get(url)
    htmlPage = str(req.content, "utf-8")
    parsableHTML = BeautifulSoup(htmlPage, features="html.parser")
    return parsableHTML.get_text()

def spiderParser(url):
    listOfLinks = initialParser(url)
    for link in listOfLinks:
        fullText = articleParser(link)
        # Do something here to transfer the full text & url to another function
        print(fullText)
        break

print(spiderParser("https://www.foxnews.com/"))


# import re
# import copy
# import requests
# import html2text
# from bs4 import BeautifulSoup, Comment, NavigableString


# class Extractor():
#     def __init__(self, html):
#         self.html = html

#     def __process_text_ratio(self, soup) -> tuple:
#         soup = copy.copy(soup)
#         if soup:
#             if type(soup) is NavigableString:
#                 return 1
#             for t in soup.find_all(['script', 'style', 'noscript', 'a', 'img']):
#                 t.extract()
#             soup_str = re.sub(r'\s*[^=\s+]+\s*=\s*([^=>]+)?(?=(\s+|>))', "", str(soup))
#             total_len = len(soup_str)
#             if total_len:
#                 tag_len = 0.0
#                 for tag in re.compile(r'</?\w+[^>]*>|[\s]', re.S).findall(soup_str):
#                     tag_len += len(tag)
#                 return (total_len-tag_len)/total_len, total_len
#         return 0, 0

#     def __find_article_html(self, soup) -> BeautifulSoup:
#         tmp_len = 0
#         tmp_tag = None
#         tmp_radio = 0.0
#         parent_radio = self.__process_text_ratio(soup)[0]
#         if not soup:
#             return None
#         if type(soup) is NavigableString:
#             return soup

#         for tag in soup.contents:
#             if tag == '\n' or not tag.name or tag.name in ['script', 'style', 'noscript', 'a']:
#                 continue
#             # double check
#             tag_radio, tag_len = self.__process_text_ratio(tag)
#             if tag_len >= tmp_len and tag_radio >= parent_radio:
#                 tmp_len = tag_len
#                 tmp_tag = tag
#                 tmp_radio = tag_radio
#         if tmp_radio == 1:
#             return soup
#         if tmp_radio >= parent_radio and tmp_tag.name != 'p':
#             # article radio
#             if soup.find_all(re.compile("h[1-6]")) or tmp_radio < self.threshold:
#                 return self.__find_article_html(tmp_tag)
#             return tmp_tag
#         else:
#             return soup

#     def parse(self) -> tuple:
#         soup = BeautifulSoup(self.html, 'lxml')
#         soup = soup.find('body')
#         if soup:
#             for tag in soup.find_all(style=re.compile('display:\s?none')):
#                 tag.extract()
#             for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
#                 comment.extract()
#             article_html = self.__find_article_html(soup)
#             if self.output == 'markdown':
#                 return self.__get_title(article_html), self.__html_to_md(article_html)
#             else:
#                 return self.__get_title(article_html), article_html
#         return '', ''

#     def __html_to_md(self, soup) -> str:
#         return html2text.html2text(str(soup), baseurl=self.url)