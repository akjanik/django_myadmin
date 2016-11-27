from django.db import models
from django.utils import timezone

class MyAdmin(models.Model):
    """
    Model to store another models
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Model1(models.Model):
    charfield1 = models.CharField(max_length=20)
    textfield1 = models.TextField()

    def __str__(self):
        return self.charfield1


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 50, blank = True)
    age = models.IntegerField()


    # def get_absolute_url(self):
    #     return url(r'^Person/(?P<pk>\d+)/$', person_detail, name="person-detail")

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length = 30)
    publication_date = models.DateField()
    page_amount = models.IntegerField()

    def __str__(self):
        return self.title
