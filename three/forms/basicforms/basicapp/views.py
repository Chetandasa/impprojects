from django.shortcuts import render
from .forms import FormName

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            # Do something with the form data
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
