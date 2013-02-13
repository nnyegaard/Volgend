__author__ = 'nnyegaard'

from behave import *

@given(u'we populated a object of the type Series with content')
def step(context):
    from VolgenModel import Series


@given(u'it\'s the first time we want to save this content')
def step(context):
    pass


@when(u'we save the content to disk')
def step(context):
    pass

@then(u'a file will be created containing our object as a json data type')
def step(context):
    pass