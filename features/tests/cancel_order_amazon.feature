# Created by Joonil at 2/2/21
Feature: Test Scenarios for Logged out user searches for how to cancel on Amazon customer service page

  Scenario: Logged out user sees how to cancel when searching for Cancel order
    Given Open Amazon Customer Service page
    When Search for Cancel order on Amazon Customer Service page
    Then How to Cancel Items or Order is shown