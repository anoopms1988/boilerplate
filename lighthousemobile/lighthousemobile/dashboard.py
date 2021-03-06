"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'lighthousemobile.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Authentication"
        self.children.append(modules.AppList(
                _('Authentication'),
                collapsible=True,
                column=1,
                css_classes=('collapse closed',),
                models=('django.contrib.*',),
        ))

        self.children.append(modules.AppList(
                _('Account'),
                collapsible=True,
                column=1,
                css_classes=('collapse closed',),
                models=('apps.account.*',),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
                _('Support'),
                column=2,
                children=[
                    {
                        'title': _('Lighthousesolar'),
                        'url': 'http://www.lighthousesolar.com/',
                        'external': True,
                    }
                ]
        ))
