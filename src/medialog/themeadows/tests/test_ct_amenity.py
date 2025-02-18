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


class AmenityIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_THEMEADOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_amenity_schema(self):
        fti = queryUtility(IDexterityFTI, name='Amenity')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Amenity')
        self.assertIn(schema_name.lstrip('plone_0_'), schema.getName())

    def test_ct_amenity_fti(self):
        fti = queryUtility(IDexterityFTI, name='Amenity')
        self.assertTrue(fti)

    def test_ct_amenity_factory(self):
        fti = queryUtility(IDexterityFTI, name='Amenity')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_amenity_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Amenity',
            id='amenity',
        )


        parent = obj.__parent__
        self.assertIn('amenity', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('amenity', parent.objectIds())

    def test_ct_amenity_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Amenity')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_amenity_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Amenity')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'amenity_id',
            title='Amenity container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
