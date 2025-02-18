# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.themeadows -t test_board_only.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.themeadows.testing.MEDIALOG_THEMEADOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/themeadows/tests/robot/test_board_only.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Board Only
  Given a logged-in site administrator
    and an add Board Only form
   When I type 'My Board Only' into the title field
    and I submit the form
   Then a Board Only with the title 'My Board Only' has been created

Scenario: As a site administrator I can view a Board Only
  Given a logged-in site administrator
    and a Board Only 'My Board Only'
   When I go to the Board Only view
   Then I can see the Board Only title 'My Board Only'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Board Only form
  Go To  ${PLONE_URL}/++add++Board Only

a Board Only 'My Board Only'
  Create content  type=Board Only  id=my-board_only  title=My Board Only

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Board Only view
  Go To  ${PLONE_URL}/my-board_only
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Board Only with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Board Only title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
