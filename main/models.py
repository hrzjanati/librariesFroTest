from django.db import models

# Create your models here.
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_of_create = models.DateField()

    def __str__(self):
        return self.name


class RequiredItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='required_items')
    name = models.CharField(max_length=255, default='Unknown')
    category = models.CharField(max_length=255)
    number_of_required = models.IntegerField()
    given_number = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.number_of_required}"


