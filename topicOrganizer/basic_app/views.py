from django.shortcuts import render
from . import forms
from basic_app.models import User

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def create(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Suc')
            form.save(commit=True)
            return index(request)
        else:
            raiseError('Invalid')
    return render(request, 'basic_app/create.html', {'form':form})

def view(request):
    data = {'data':User.objects.order_by('name')}
    return render(request, 'basic_app/view.html', data)
