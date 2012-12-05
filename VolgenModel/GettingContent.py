__author__ = 'nnyegaard'


import logging
from pyquery import PyQuery as pq
import re


logging.basicConfig(filename='GettingContent.log', level=logging.DEBUG)


def RemoveDuplicates(seq, idfun=None):
    """
    TODO: Write doc string
    """
# order preserving
    if idfun is None:
        def idfun(x):
            return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        result.append(item)
    logging.info(result)
    return result


def DownloadLinks(site):
    """
    Downloading all the links on a site and returning the text of the links.
    """
    if site != "":
        linksOnSite = pq(url=site, parser="html")
        return linksOnSite("a")


def ExtractSiteContent(site, keyword):
    """
    TODO: Write doc string
    """
    # With case insensitive: "[Ff]airy [Tt]ail\s\d+".
    # The parameter re.I should do that but it ain't working
    # TODO: Find the parameter to make regex case insensitive
    regex = re.compile(keyword + "\s\d+")
    links = DownloadLinks(site)
    eps = []
    if keyword != "":
        for x in links:
            # regex.findall(links(x).text()) #links(x).text() == keyword:
            if regex.match(links(x).text()):
                eps.append(int(re.search('\d+', links(x).text()).group()))
    logging.info(eps)
    return RemoveDuplicates(eps)

if __name__ == '__main__':
    print "Running a quick test, but please use behave as a definitely test."
    url = "http://www.mangareader.net/135/fairy-tail.html"
    keyword = "Fairy Tail"
    d = ExtractSiteContent(url, keyword)
    print sorted(d, key=int)
