from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        if role == 'customer':
            email = request.POST.get('customerEmail')
            

        elif role == 'hotel':
            email = request.POST.get('hotelEmail')
            

        return HttpResponse(f'Registration successful for {role}')

    return render(request, 'registration_form.html')



