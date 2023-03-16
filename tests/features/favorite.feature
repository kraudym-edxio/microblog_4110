Feature: Favrotie Status

  Scenario Outline: Successful login
    Given I am on the login page
    When I enter <type> login credentials
    And click the login button
    Then I should be redirected to the dashboard page
    # And I should see a welcome message with my username
      
    Given I have posted a status update
    When I click on the fav button next to the status update
    Then I move to Favorite section
    And I see the new status in favorite section

    Examples: 
      | type      |
      | valid     |