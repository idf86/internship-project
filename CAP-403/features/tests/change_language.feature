# Created by Windy at 12/19/23
Feature: Test Scenarios for language change

  Scenario: User can change the language from the page
    Given Open the main page
    When Log in to the page
    And Change the language of the page to Russian. The option will be “RU” is the list of the languages
    Then Verify the language has changed