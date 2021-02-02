# Created by Joonil at 2/2/21
Feature: Test Scenarios for Logged out user clicks on the shopping cart and verifies Shopping Cart is empty

  Scenario: Logged out user sees empty shopping cart when click on the shopping cart icon
    Given Open Amazon page
    When Click on the shopping cart icon
    Then Empty shopping cart is shown