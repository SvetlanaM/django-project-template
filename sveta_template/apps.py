from django.conf import settings
from django.contrib.admin.apps import AdminConfig


class SvetaAdminConfig(AdminConfig):
    default_site = settings.ADMIN_PAGE
