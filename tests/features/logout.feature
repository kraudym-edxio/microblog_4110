Feature: Logout

    Scenario Outline: Successful logout
        Given I am on the login page
        When I enter credentials <username> and <password>
        And click the login button
        Then I should be redirected to the dashboard page
        And when I click the logout button
        Then I should be redirected to the Sign In page
        
    Examples:
        | username      |   password      |
        | test714       |   test714       |

