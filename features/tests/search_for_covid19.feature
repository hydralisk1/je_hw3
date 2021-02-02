# Created by Joonil at 2/2/21
Feature: Test Scenarios for user googles COVID 19 and verifies COVID 19 alert on the search result page

  Scenario: User sees COVID 19 alert when search for COVID 19 on Google
    Given Open Google page
    When Search for COVID 19 on Google
    Then COVID 19 alert is shown on the search result page