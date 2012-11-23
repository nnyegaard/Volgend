Feature: When we have extracted the content of a site, we want to filter the eps so we don't have duplicates.

We want to be able to filter the eps of the extracted site, so that we later can work with the data. One of the things
we want to be able to do is compare the latest eps in our saved data vs the one we get from the site.

Scenario: Filtering the content we have extracted from a site
    Given we have a list containing duplicates
    When we call the filter method
    Then we get a list of eps that don't contain duplicates