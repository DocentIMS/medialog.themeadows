# -*- coding: utf-8 -*-
from medialog.themeadows.testing import MEDIALOG_THEMEADOWS_FUNCTIONAL_TESTING
from medialog.themeadows.testing import MEDIALOG_THEMEADOWS_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_THEMEADOWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_meadows_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='meadows-view'
        )
        self.assertTrue(view.__name__ == 'meadows-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in meadows-view'
        # )

    def test_meadows_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='meadows-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = MEDIALOG_THEMEADOWS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
