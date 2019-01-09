import urllib2


class UsingUrllib2():
    #To use a proxy just call this function before calling the first websit
    def useProx(self):
        proxy = urllib2.ProxyHandler({
            'http': 'xxx.xxx.xxx.xxx',
            'https': 'xxx.xxx.xxx.xxx'
        })
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

    # Call a website and return the response
    def getPage(self, url):
        try:
            #self.useProx()
            page = urllib2.urlopen(url)
            return page
        except:
            print " Error in webReq"