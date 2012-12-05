Feature: We want to be able to encode and decode our data into json data so we can save the json data to a file.

Scenario: Encoding object into json
    Given we have a python object we want to encode into a json object
    When we call the encoding function
    Then we get a json object

Scenario: Decoding object into json
    Given we have a json object we want to decode into a python object
    When we call the decoding function
    Then we can create a python object out from the json object