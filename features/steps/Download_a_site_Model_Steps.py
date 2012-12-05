__author__ = 'nnyegaard'

from behave import *

@given(u'we have the model PyQuery installed')
def step(context):
    try:
        import pyquery
    except ImportError, e:
        assert e is False

@when(u'we call the method \"Download_site(url)\"')
def step(context):
    from VolgenModel import GettingContent
    context.site = GettingContent.DownloadLinks("http://mangastream.com/")

@then(u'we should get a list that are not empty')
def step(context):
    assert context.site != []

