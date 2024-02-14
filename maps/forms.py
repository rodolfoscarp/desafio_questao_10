from django.forms import ModelForm

from .models import Locais


class CreateLocalForm(ModelForm):
    class Meta:
        model = Locais
        fields = ['nome', 'latitude', 'longitude', 'data_expiracao']
