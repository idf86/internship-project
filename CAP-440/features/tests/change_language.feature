# Created by Svetlana at 4/4/19
Feature: Test Scenarios for language change

  Scenario: User can change the language from the page
    Given Open the main page
    When Log in to the page
    And Change the language of the page to Russian. The option will be “Русский” is the list of the languages
    Then Verify the language has changed