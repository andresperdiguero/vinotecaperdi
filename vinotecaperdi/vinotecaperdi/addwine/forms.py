from django.forms import ModelForm
from django.db import models
from vinotecaperdi.addwine.models import Wine, Rate


class AddWineForm(ModelForm):
    name_wine = models.CharField(max_length=50)

    class Meta:
        model = Wine
        fields = ('name_wine', 'winery', 'harvest', 'varietal')

class VoteWineForm(ModelForm):
    class Meta:
        model = Rate
        fields = ('name_wine', 'rate')
