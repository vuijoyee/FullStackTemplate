from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm


# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Rambod Ghashghai'
    args = {'myName': name, 'numbers': numbers}
    return render(request ,'accounts/home.html',args)
    #return HttpResponse('Home Page')

def login(request):
    return render(request,'accounts/login.html')

def regsiter(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()



        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)
