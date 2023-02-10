from django.db import models


class Schedule(models.Model):
    subject_name = models.CharField(max_length=128)
    is_passed = models.BooleanField("Здано", default=False)

    def __str__(self):
        return self.subject_name
