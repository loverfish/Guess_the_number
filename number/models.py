from django.db import models


class Number(models.Model):
    numb = models.IntegerField()
    digits_quantity = models.IntegerField(null=True)

    def __str__(self):
        return str(self.numb)
