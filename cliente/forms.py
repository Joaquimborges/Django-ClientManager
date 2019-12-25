from django.forms import ModelForm
from .models import Person


class PersonForms(ModelForm): #deverá ser importado para a views
    class Meta:
        model = Person
        fields = ['primeiro_nome', 'ultimo_nome', 'idade', 'salario', 'bio', 'foto'] #campos existentes no formulário