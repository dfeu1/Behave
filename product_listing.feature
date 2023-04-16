Feature: Testing Search at Nike

  Scenario: Search for Jordan 1 on Nike.com
    Given I am on the Nike website
    When When I search for "Jordan 1"
    Then I should see the first shoe in the search results

  Scenario: Search for Dunks on Nike.com
    Given I am on the Nike website
    When When I search for "Dunks"
    Then I should see the first shoe in the search results

  Scenario: Search for mens black Dunks on Nike.com
    Given I am on the Nike website
    When When I search for "mens black Dunks"
    Then I should see the first shoe in the search results