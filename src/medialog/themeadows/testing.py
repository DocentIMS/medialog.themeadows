# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.themeadows


class MedialogThemeadowsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.themeadows)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.themeadows:default')


MEDIALOG_THEMEADOWS_FIXTURE = MedialogThemeadowsLayer()


MEDIALOG_THEMEADOWS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_THEMEADOWS_FIXTURE,),
    name='MedialogThemeadowsLayer:IntegrationTesting',
)


MEDIALOG_THEMEADOWS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_THEMEADOWS_FIXTURE,),
    name='MedialogThemeadowsLayer:FunctionalTesting',
)


MEDIALOG_THEMEADOWS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_THEMEADOWS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogThemeadowsLayer:AcceptanceTesting',
)
