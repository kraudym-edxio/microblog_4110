Feature: Status Reactions

  Scenario Outline: Successful login
    Given I am on the login page
    When I enter <type> login credentials
    And click the login button
    Then I should be redirected to the dashboard page
    # And I should see a welcome message with my username
      
    Given I have posted a status update
    And I go to explore
    When I click on the fav button next to the status update I want to delete
    Then the fav counter next to the react emoji should be updated
    Examples: 
      | type    | 
      | valid   |