import psycopg2
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def add_shuttle(request):
    connection = psycopg2.connect(
        dbname='railway',
        user='postgres',
        password='EcgcG5CGgE6b3B6B4EBaaGb-F16fddcb',
        host='viaduct.proxy.rlwy.net',
        port='57165'
    )
    cursor = connection.cursor()
        
    query = 'set search_path to sistel;'
    
    query += """
            select distinct concat(vehicle_brand, ' ', vehicle_type)
            from vehicle
            where platnum not in (
                select vehicle_num
                from reservation_shuttleservice
                where isActive = true
            );
            """

    cursor.execute(query)

    # Fetch hasilnya
    results = cursor.fetchall()

    for i in range(len(results)):
        results[i] = results[i][0]

    print(results)

    # Jangan lupa menutup koneksi
    connection.close()

    return render(request, "add_shuttle.html", {'kendaraan' : results})

def add_complaint(request):
    return render(request, "add_complaint.html", {})

def add_review(request):
    return render(request, "add_review.html", {})

@csrf_exempt
def reservation_submit(request):
    if request.method == 'POST':
        # Proses data formulir yang dikirim
        vehicle_selected = request.POST.get('vehicle')
        # Lakukan sesuatu dengan data formulir (contoh: mencetak ke konsol)
        print("Selected Vehicle:", vehicle_selected)
        return HttpResponse(b"RETURNED", status=201)

    return HttpResponseNotFound()