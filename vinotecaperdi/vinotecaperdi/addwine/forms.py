from django.forms import ModelForm
from django.db import models
from vinotecaperdi.addwine.models import Wine


class AddWineForm(ModelForm):
    name_wine = models.CharField(help_text='Required', max_length=50)

    class Meta:
        model = Wine
        fields = ('name_wine', 'winery', 'harvest', 'varietal')
