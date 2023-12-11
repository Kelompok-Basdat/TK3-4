from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection as conn
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


def show_landingpage(request):
    context = {}
    return render(request, "landingpage.html", context)



def login_user(request):
    return render(request, 'login.html', {})

@csrf_exempt
def login(request):
    print(69)
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        print(username, password)
        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     if user.groups.filter(name='Admin').exists():
        #         return redirect('admin_dashboard')
        #     elif user.groups.filter(name='Customer').exists():
        #         return redirect('Customer_dashboard')
        #     elif user.groups.filter(name='Hotel').exists():
        #         return redirect('Hotel_dashboard')
        #     else:
        #         # Handle other roles or default redirect
        #         return redirect('home')
        # else:
        #     messages.error(request, "Invalid Account")
        #     return redirect('login')
    return HttpResponseNotFound()

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')