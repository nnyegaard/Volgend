Feature: Connecting to a site to get the HTML content

Before we can traverse a site for content we need to download the site.

Scenario: Downloading a site
    Given we have the model PyQuery installed
    When we call the method "Download_site(url)"
    Then we should get a list that are not empty

Scenario: Searching for content on a site based on a keyword
    Given we have downloaded a site
    And we have a keyword present
    When we extract the content based on the site
    Then we should get a list containing numbers
