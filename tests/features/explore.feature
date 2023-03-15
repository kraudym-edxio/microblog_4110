Feature: Explore

    Scenario Outline: Successful post on explore
        Given I am on the main page
        When I enter the <text> for my post
        And click submit button
        Then I should be seeing a message saying my post is live
        And when I click the explore 
        Then my <text> should appear in the list
    Examples:
        | text      |
        | Taxi10!     |