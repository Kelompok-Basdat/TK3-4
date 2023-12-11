from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def show_landingpage(request):
    context = {
    }
    return render(request, "landingpage.html", context)



def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.groups.filter(name='Admin').exists():
                    return redirect('admin_dashboard')
                elif user.groups.filter(name='Customer').exists():
                    return redirect('Customer_dashboard')
                elif user.groups.filter(name='Hotel').exists():
                    return redirect('Hotel_dashboard')
                else:
                    # Handle other roles or default redirect
                    return redirect('home')
            else:
                messages.error(request, "Invalid Account")
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')