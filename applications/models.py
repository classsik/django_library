from django.db import models


class Application(models.Model):
    date_take = models.DateField() #хранит дату когда возьмет
    date_give = models.DateField() #хранит дату когда отдаст
    comment = models.CharField(max_length=200)


