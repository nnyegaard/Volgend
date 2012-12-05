__author__ = 'nnyegaard'

from behave import *
from VolgenModel.Series import ASeries
import json

@given(u'we have a python object we want to encode into a json object')
def step(context):
    context.TheSeries = ASeries
    context.TheSeries.name = "Awesome!"
    context.TheSeries.eps = [1, 2, 3]
    context.TheSeries.rating = 5

@when(u'we call the encoding function')
def step(context):
    from VolgenModel.JsonConvertion import SeriesEncoder

    context.jsonEncodedData = json.dumps(SeriesEncoder().encode((context.TheSeries.name, context.TheSeries.eps, context.TheSeries.rating)))

@then(u'we get a json object')
def step(context):
    assert context.jsonEncodedData[0] != None


@given(u'we have a json object we want to decode into a python object')
def step(context):
    context.TheSeries = ASeries()
    context.TheSeries.name = "Awesome!"
    context.TheSeries.eps = [1, 2, 3]
    context.TheSeries.rating = 5

    from VolgenModel.JsonConvertion import SeriesEncoder

    context.jsonEncodedData = SeriesEncoder().encode((context.TheSeries.name, context.TheSeries.eps, context.TheSeries.rating))
    assert context.jsonEncodedData[0] != None

@when(u'we call the decoding function')
def step(context):
    context.jsonDecodedData = json.loads(context.jsonEncodedData)

@then(u'we can create a python object out from the json object')
def step(context):
    MySeries = ASeries()
    MySeries.name = context.jsonDecodedData[0]
    MySeries.eps = context.jsonDecodedData[1]
    MySeries.rating = context.jsonDecodedData[2]

    assert MySeries.name == "Awesome!"
    assert MySeries.eps == [1, 2, 3]
    assert MySeries.rating == 5

