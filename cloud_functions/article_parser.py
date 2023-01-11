import requests # Allows us to get the actual HTML page
from bs4 import BeautifulSoup # Spider / WebCrawler

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
    return

spiderParser("https://www.foxnews.com/")