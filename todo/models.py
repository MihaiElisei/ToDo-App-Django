from django.db import models

# Create your models here.


class Item(models.Model):
    # create Item model table
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # return the name of the Items in table
    def __str__(self):
        return self.name
