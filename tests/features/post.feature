Feature: Post

    Scenario Outline: Successful post
        Given I am on the home page
        When I enter <text> for my post
        And click the submit button
        Then I should be see a message saying my post is live
    Examples:
        | text      |   Hello World!      |
