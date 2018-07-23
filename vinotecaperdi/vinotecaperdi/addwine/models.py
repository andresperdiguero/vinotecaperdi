from django.db import models

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Wine (models.Model):
    user_name=models.CharField(max_length=20, default='')
    name_wine=models.CharField(max_length=50)
    winery=models.CharField(max_length=50)
    harvest=models.IntegerField(('harvest'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    varietal=models.CharField(max_length=30)
