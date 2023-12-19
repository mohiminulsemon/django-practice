from django.shortcuts import render
from . forms import contactForm

# Create your views here.


def form_fields(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, './form.html', {'form': form})