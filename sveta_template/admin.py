from typing import Any

from django.contrib.admin.sites import AdminSite

from utils.mixins import with_typehint

# https://github.com/python/mypy/issues/2477#issuecomment-262734005
BaseAdminSite = with_typehint(AdminSite)  # type: Any


class AdminSiteMixin(BaseAdminSite):
    def each_context(self, request):
        if not request.user.is_superuser:
            return super().each_context(request)

        return super().each_context(request)


class SvetaAdmin(AdminSiteMixin, AdminSite):
    pass
