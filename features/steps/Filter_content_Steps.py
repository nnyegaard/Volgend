__author__ = 'nnyegaard'

from behave import *
from VolgenModel import GettingContent


@given(u'we have a list containing duplicates')
def step(context):
    context.dupList = [1, 2, 3, 1, 2, 3]


@when(u'we call the filter method')
def step(context):
    context.cleanList = GettingContent.RemoveDuplicates(context.dupList)


@then(u'we get a list of eps that don\'t contain duplicates')
def step(context):
    assert context.cleanList == [1, 2, 3]