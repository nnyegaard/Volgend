Feature: When we have extracted the content of a site, we want to save it for later use.

Scenario: Saving our content to disk, for the first time
    Given we have extracted the content of a site, that are contained in a list
    And it's the first time we want to save this content
    When we save the content to disk
    Then a file will be created containing a list of eps