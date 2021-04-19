from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Number(models.Model):
    numb = models.IntegerField()
    digits_quantity = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(15)],
    )

    def __str__(self):
        return str(self.numb)
