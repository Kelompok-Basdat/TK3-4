from django.shortcuts import render

# Create your views here.
def find_hotel(request):
    return render(request, "search_hotel.html", {})

def specific_hotel(request):
    return render(request, "specific_hotel.html", {})

def fasilitas_hotel(request):
    return render(request, "fasilitas.html", {})

def create_fasilitas_hotel(request):
    return render(request, "create_fasilitas.html", {})

def update_fasilitas_hotel(request):
    return render(request, "update_fasilitas.html", {})