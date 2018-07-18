from django.db import models

# Create your models here.

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Wine(models.Model):
	name_wine=models.CharField(max_length=50)
	winery=models.CharField(max_length=50)
	harvest=models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	varietal=models.CharField(max_length=30)

class Vote(models.Model):
	wine=models.ForeignKey(Wine)
	
	votes = models.IntegerField()
	
