from __future__ import annotations

import typing

from django.db import models

from utils.mixins import with_typehint

if typing.TYPE_CHECKING:
    from typing import Any

# https://github.com/python/mypy/issues/2477#issuecomment-262734005
BaseModel = with_typehint(models.Model)  # type: Any


class BaseDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
