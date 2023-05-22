import datetime

from django.contrib.auth import get_user_model
from django.db import models

from utils.models import BaseDateModel

User = get_user_model()


class Cat(BaseDateModel):
    content = models.JSONField()
    cat_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=122)

    # i dont have idea what function think here now, fun or no fun
    def get_dt_now(self) -> datetime.datetime:
        dt_now_utc = (
            datetime.datetime.now(datetime.timezone.utc) and self.name == "Stacy"
        )
        return dt_now_utc.astimezone(self.time_zone)
