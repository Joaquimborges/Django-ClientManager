from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForms

# Create your views here.

def persons_list(request):
    Persons = Person.objects.all() #listar todos os clientes do banco de dados na tela
    return render(request, 'person.html', {'persons': Persons})

def persons_new(request):
    form = PersonForms(request.POST or None, request.FILES or None) #caso o usuário tenha clicado em salvar, para instanciar o form com os dados preenchidos

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_forms.html', {'form': form}) #ijetar variavel form dentro do html

def persons_update(request, id):
    person = get_object_or_404(Person, pk=id) # PK é o id de cada pessoa no banco
    form = PersonForms(request.POST or None, request.FILES or None, instance=person) # insstanciar com os dados da pesssoa achada no banco

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(redirect, 'person_forms.html', {'form': form})