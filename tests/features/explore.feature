Feature: Post

    Scenario Outline: Successful post on explore
        Given I am on the home page
        When I enter <text> for my post
        And click the submit button
        Then I should be see a message saying my post is live
        And when I click the explore 
        Then my post should appear in the list
    Examples:
        | text      |   Taxi!      |