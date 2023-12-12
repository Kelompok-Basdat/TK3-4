from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection as conn
from django.http import (HttpResponseNotFound, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def show_landingpage(request):
    context = {}
    return render(request, "landingpage.html", context)



def login_user(request):
    if 'user' in request.session:
        return redirect('dashboard:show_dashboard')
    return render(request, 'login.html', {})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        with conn.cursor() as cursor:
            cursor.execute("set search_path to sistel;")
            cursor.execute("select * from sistel.user where email=%s;", (email,))
            user = cursor.fetchone()
            if not user or user[1] != password:
                return JsonResponse({"status": "error", "message": "Invalid Email or Password"})
            else:
                cursor.execute("set search_path to public;")
                request.session['user'] = email
                cursor.execute('select hotel_name, hotel_branch from sistel.hotel where email = %s' , (email,))
                res = cursor.fetchone()
                if res:
                    request.session['hotel_name'] = res[0]
                    request.session['hotel_branch'] = res[1]
                return JsonResponse({"status": "success"})
                
    return HttpResponseNotFound()

def logout_user(request):
    if 'user' in request.session:
        request.session.flush()
    messages.success(request, ("You Were Logged Out!"))
    return redirect('login:show_landingpage')