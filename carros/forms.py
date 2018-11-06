from django.forms import ModelForm

from carros.models import Cor
from .models import Montadora


class MontadoraForm(ModelForm):
    class Meta:
        model = Montadora
        fields = '__all__'


class CorForm(ModelForm):
    class Meta:
        model = Cor
        fields = '__all__'
