###### Copyright ##################
__author__ = 'nnyegaard'          #
###################################

###### Imports ####################
import logging                    #
from pyquery import PyQuery as pq #
import re                         #
###################################

logging.basicConfig(filename='Model.log',level=logging.DEBUG)

def Remove_Duplicates(seq, idfun=None):
# order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    logging.info(result)
    return result

def Download_Links(site):
    """
    Downloading all the links on a site and returning the text of the links.
    """
    if site != "":
        linksOnSite = pq(url=site, parser="html")
        return linksOnSite("a")


def Extract_Site_Content(site, keyword):
    """

    """
    regex = re.compile(keyword+"\s\d+") #With case insensitive: "[Ff]airy [Tt]ail\s\d+" The parameter re.I should do that but it ain't working TODO: Find the parameter to make regex case insensitive
    links = Download_Links(site)
    eps = []
    if keyword != "":
        for x in links:
            if regex.match(links(x).text()):#regex.findall(links(x).text()) #links(x).text() == keyword:
                eps.append(int(re.search('\d+',links(x).text()).group()))
                #print int(re.search('\d+',links(x).text()).group())
    logging.info(eps)
    return Remove_Duplicates(eps)



if __name__ == '__main__':
    print "Running a quick test, but please use behave as a definitely test."
    d = Extract_Site_Content("http://www.mangareader.net/135/fairy-tail.html", "Fairy Tail")
    print sorted(d,key=int)

