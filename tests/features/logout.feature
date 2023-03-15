Feature: Logout

    Scenario Outline: Successful logout
        Given I am in the login page
        When I enter my credentials <username> and <password>
        And I click the login button
        Then I should be redirected to the main page
        And when I click the logout button
        Then I should be redirected to the Sign In page
        
    Examples:
        | username      |   password      |
        | test714       |   test714       |

