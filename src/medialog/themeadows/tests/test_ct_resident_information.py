# -*- coding: utf-8 -*-
from medialog.themeadows.testing import MEDIALOG_THEMEADOWS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class ResidentInformationIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_THEMEADOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_resident_information_schema(self):
        fti = queryUtility(IDexterityFTI, name='Resident Information')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Resident Information')
        self.assertIn(schema_name.lstrip('plone_0_'), schema.getName())

    def test_ct_resident_information_fti(self):
        fti = queryUtility(IDexterityFTI, name='Resident Information')
        self.assertTrue(fti)

    def test_ct_resident_information_factory(self):
        fti = queryUtility(IDexterityFTI, name='Resident Information')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_resident_information_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Resident Information',
            id='resident_information',
        )


        parent = obj.__parent__
        self.assertIn('resident_information', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('resident_information', parent.objectIds())

    def test_ct_resident_information_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Resident Information')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
