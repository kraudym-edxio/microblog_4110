Feature: Delete Status

  Scenario Outline: Successful login
    Given I am on the login page
    When I enter <type> login credentials
    And click the login button
    Then I should be redirected to the dashboard page
    # And I should see a welcome message with my username
      
    Given I have posted a status update
    # And I am viewing my status updates
    When I click on the delete button next to the status update I want to delete
    Then the status update should be permanently removed from my profile

    Examples: 
      | type      |
      | valid     |
