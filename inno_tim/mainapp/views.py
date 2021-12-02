from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.forms import StartupForm


def startup(request):
    if request.method == 'POST':
        form = StartupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:startup'))
    else:
        form = StartupForm()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/startup.html', context)
