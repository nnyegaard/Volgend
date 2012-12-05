__author__ = 'nnyegaard'

import json
from Series import ASeries


class SeriesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ASeries):
            return [obj.eps, obj.name, obj.rating]
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    print "Running a quick test, but please use behave as a definitely test."
    awesome = ASeries()
    awesome.name = "Awesome!"
    awesome.eps = [1, 2, 3]
    awesome.rating = 3

    jsonEncodedData = SeriesEncoder().encode((awesome.name, awesome.eps, awesome.rating))
    jsonDecodedData = json.loads(jsonEncodedData)

    print "Json encoded data: ", jsonEncodedData
    print "Json Decoded data: ", jsonDecodedData

    awesome2 = ASeries()
    awesome2.name = jsonDecodedData[0]
    awesome2.eps = jsonDecodedData[1]
    awesome2.rating = jsonDecodedData[2]

    print "Json to python name: ", awesome2.name

