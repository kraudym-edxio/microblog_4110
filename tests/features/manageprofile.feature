Feature: Manage Profile

    Scenario Outline: Successful Profile Update
        Given I am on my user home page
        And I click Profile
        And I click Edit Your Profile
        When I enter new profile information <username> and <aboutme>
        And I click Submit
        Then I should see a confirmation message at the top
        And When I return to my profile
        Then I should see my profile information changed
    Examples:
        | username      |   aboutme     |
        | test502       |   test502      |

