Feature: Login

    Scenario: Successful login
        Given I am on the login page
        When I enter my valid credentials
        And click the login button
        Then I should be redirected to the dashboard page
        And I should see a welcome message with my username