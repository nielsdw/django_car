from django.forms import ModelForm
from onzeapp.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
