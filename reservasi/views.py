from django.shortcuts import render


# Create your views here.
def add_shuttle(request):
    return render(request, "add_shuttle.html", {})

def add_complaint(request):
    return render(request, "add_complaint.html", {})

def add_review(request):
    return render(request, "add_review.html", {})