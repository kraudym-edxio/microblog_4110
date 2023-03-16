Feature: Logout

    Scenario Outline: Successful logout
        Given I am in the login page
        When I enter <type> login credentials
        And I click the login button
        Then I should be redirected to the main page
        And when I click the logout button
        Then I should be redirected to the Sign In page

    Examples: 
      | type      |
      | valid     |