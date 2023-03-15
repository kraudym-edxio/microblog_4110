Feature: Register

    Scenario Outline: Successful register
        Given I am on the registration page
        When I enter the credentials <username>, <email> and <password>
        And click the Register Button
        Then I should be redirected to Sign In page
        And I should see a congratulations
    Examples:
        | username      |  email      | password      |
        | test712       |  tst@a.ca   | test715       |

    Scenario Outline: Unsuccessful register
        Given I am on the registration page
        When I enter credentials <username>, <email> and <password>
        And click the Register Button
        Then I should see an error message
    Examples:
        | username      |  email      | password      |
        | test714       |  tst1       | test715       |