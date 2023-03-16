Feature: Login

  Scenario Outline: Successful login
    Given I am on the login page
    When I enter <type> login credentials
    And click the login button
    Then I should be redirected to the dashboard page
    And I should see a welcome message with my username
    Examples: 
      | type      |
      | valid     |

  Scenario Outline: Unsuccessful login
    Given I am on the login page
    When I enter <type> login credentials
    And click the login button
    Then I should see an error

    Examples: 
      | type      |
      | invalid   |
