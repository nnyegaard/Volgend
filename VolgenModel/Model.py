###### Copyright ##################
__author__ = 'nnyegaard'          #
###################################

###### Imports ####################
import logging                    #
from pyquery import PyQuery as pq #
import re                         #
###################################

logging.basicConfig(filename='Model.log',level=logging.DEBUG)

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
    if keyword != "":
        for x in links:
            if regex.match(links(x).text()):#regex.findall(links(x).text()) #links(x).text() == keyword:
                logging.info(int(re.search('\d+',links(x).text()).group()))
                return [token for token in links(x).text().split(" ") if token.isdigit()] #With a regex: int(re.search('\d+',links(x).text()).group())


if __name__ == '__main__':
    Extract_Site_Content("http://www.mangareader.net/135/fairy-tail.html", "Fairy Tail")