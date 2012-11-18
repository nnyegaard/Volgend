__author__ = 'nnyegaard'

from behave import *

@given("we have the model request installed")
def step(context):
    try:
        import requests
    except ImportError, e:
        assert e is False

@when("we call the method \"Download_site(url)\"")
def step(context):
    from VolgenModel import Model
    context.site = Model.Download_site("https://www.google.com/")

@then("we should not get an exception")
def step(context):
    assert context.site != Exception

