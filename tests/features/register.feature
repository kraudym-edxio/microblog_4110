Feature: Register

    Scenario Outline: Successful register
        Given I am on the registration page
        When I enter <type> registration credentials
        And click the Register Button
        Then I should be redirected to Sign In page
        And I should see a congratulations
    Examples: 
      | type    | 
      | valid   |

    Scenario Outline: Unsuccessful register
        Given I am on the registration page
        When I enter <type> registration credentials
        And click the Register Button
        Then I should see an error message
    Examples: 
      | type    | 
      | invalid   |