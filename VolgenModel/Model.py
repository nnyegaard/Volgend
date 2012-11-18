###### Copyright ########
__author__ = 'nnyegaard'#
#########################

###### Imports ######
import requests     #
import logging      #
#####################

logging.basicConfig(filename='Model.log',level=logging.DEBUG)

def Download_site(url):
    """
    Downloading a site and returning the text of the given site.
    Using a simple check for the status code to see if we got the site
    """
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception("We did not get a status code of 200. The site may be down.")
    else:
        return r.text


def Extract_Site_Content(url, keyword):
    """

    """
    site = Download_site(url)
    if keyword != "":
        pass