# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.themeadows -t test_resident_information.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.themeadows.testing.MEDIALOG_THEMEADOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/themeadows/tests/robot/test_resident_information.robot
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

Scenario: As a site administrator I can add a Resident Information
  Given a logged-in site administrator
    and an add Resident Information form
   When I type 'My Resident Information' into the title field
    and I submit the form
   Then a Resident Information with the title 'My Resident Information' has been created

Scenario: As a site administrator I can view a Resident Information
  Given a logged-in site administrator
    and a Resident Information 'My Resident Information'
   When I go to the Resident Information view
   Then I can see the Resident Information title 'My Resident Information'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Resident Information form
  Go To  ${PLONE_URL}/++add++Resident Information

a Resident Information 'My Resident Information'
  Create content  type=Resident Information  id=my-resident_information  title=My Resident Information

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Resident Information view
  Go To  ${PLONE_URL}/my-resident_information
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Resident Information with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Resident Information title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
