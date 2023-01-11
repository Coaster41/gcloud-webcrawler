import requests # Allows us to get the actual HTML page
from bs4 import BeautifulSoup # Spider / WebCrawler

def filterFunct(myArray):
    for link in myArray:
        if link == "None":
            pass


def spiderParser(myUrl):
    req = requests.get(myUrl) # Get HTML Page
    htmlPage = str(req.content, "utf-8") # Stringify HTML page
    parsableHTML = BeautifulSoup(htmlPage, 'html.parser') # Make the HTML page a Soup Class

    myArray = []

    # for link in parsableHTML.find_all('a'):
    #     print(link)
    #     myArray.append(link.get('href'))
    
    fullReturnedText = parsableHTML.prettify()
    # myArray.filter(filterFunct, myArray)


    return fullReturnedText

print(spiderParser("https://www.cnn.com/"))