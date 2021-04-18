from django.db import models


class Number(models.Model):
    numb = models.IntegerField()

    def __str__(self):
        return str(self.numb)
