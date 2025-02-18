# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.themeadows -t test_amenity.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.themeadows.testing.MEDIALOG_THEMEADOWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/themeadows/tests/robot/test_amenity.robot
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

Scenario: As a site administrator I can add a Amenity
  Given a logged-in site administrator
    and an add Amenity form
   When I type 'My Amenity' into the title field
    and I submit the form
   Then a Amenity with the title 'My Amenity' has been created

Scenario: As a site administrator I can view a Amenity
  Given a logged-in site administrator
    and a Amenity 'My Amenity'
   When I go to the Amenity view
   Then I can see the Amenity title 'My Amenity'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Amenity form
  Go To  ${PLONE_URL}/++add++Amenity

a Amenity 'My Amenity'
  Create content  type=Amenity  id=my-amenity  title=My Amenity

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Amenity view
  Go To  ${PLONE_URL}/my-amenity
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Amenity with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Amenity title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
