from bs4 import BeautifulSoup

class UsingBsSoup():

    #Get soup object from website
    def getBeautifulSoupObj(self, html):
        soup = BeautifulSoup(html)
        #print soup.prettify()
        return soup