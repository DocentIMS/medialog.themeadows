# -*- coding: utf-8 -*-

# from medialog.themeadows import _
from Products.Five.browser import BrowserView
from zope.interface import Interface
from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAminityView(Interface):
    """ Marker Interface for IAminityView"""


class AminityView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('aminity_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
    
    # def get_items(self):
    #     return api.content.find(portal_type='Aminity')
