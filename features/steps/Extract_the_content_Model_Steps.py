__author__ = 'nnyegaard'

from behave import *
from VolgenModel import GettingContent

@given(u'we have downloaded a site')
def step(context):
    assert GettingContent.DownloadLinks("http://www.mangareader.net/135/fairy-tail.html") != []


@given(u'we have a keyword present')
def step(context):
    context.keyword = "Fairy Tail"


@when(u'we extract the content based on the site')
def step(context):
    context.content = GettingContent.ExtractSiteContent("http://www.mangareader.net/135/fairy-tail.html", context.keyword)


@then(u'we should get a list containing numbers')
def step(context):
    assert context.content != []
    assert isinstance(context.content[0], int)

