from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm
def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')  
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})
