from django.db import models

# Create your models here.
class SnakesManager(models.Manager):
    def snake_validate(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "Name must be at least 3 characters long."
        if len(postData['length']) < 1:
            errors['length'] = "You must add a length."
        return errors


class Snake(models.Model):
    name = models.CharField(max_length=45)
    length = models.IntegerField()
    venomous = models.BooleanField(default=False)
    objects = SnakesManager()
