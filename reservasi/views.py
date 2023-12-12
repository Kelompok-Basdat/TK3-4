import datetime

import psycopg2
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_connection():
    return psycopg2.connect(
        dbname='railway',
        user='postgres',
        password='EcgcG5CGgE6b3B6B4EBaaGb-F16fddcb',
        host='viaduct.proxy.rlwy.net',
        port='57165'
    )

def add_shuttle(request):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor = conn.cursor()
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
            results = cursor.fetchall()

            for i in range(len(results)):
                results[i] = results[i][0]
            print(results)
            if not results:
                results = ["Mohon maaf, semua kendaraan sedang terpakai.",]
            # TODO: connect reservation idnya
            rsv_id = '4235' # note: masih dummy
            context = {
                'kendaraan' : results,
                'rsv_id' : rsv_id,
            }

    return render(request, "add_shuttle.html", context)

@csrf_exempt
def add_shuttle_submit(request):
    if request.method == 'POST':
        rsv_id = request.POST.get('rsv_id')
        vehicle_selected = request.POST.get('vehicle')
        print("Selected Vehicle:", vehicle_selected)
        if vehicle_selected is not None:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute('set search_path to sistel;')
                    query =f"""
                            select driver_phonenum, vehicle_platnum
                            from shuttle_service, vehicle
                            where vehicle_platnum = platnum and concat(vehicle_brand, ' ', vehicle_type) = %s;
                            """
                    cursor.execute(query,(vehicle_selected,))
                    result = cursor.fetchall()[0]
                    print(result)
                    query = f"""
                            insert into reservation_shuttleservice (rsv_id,driver_phonenum,vehicle_num,datetime,isactive)
                            values (%s,%s,%s,%s,%s)
                            """
                    try:
                        cursor.execute(query, (rsv_id, result[0], result[1], datetime.datetime.now(), True))
                    except Exception as e:
                        error_msg = str(e).split('\n')[0]
                        return JsonResponse({"status": "error", "message": error_msg})
            return JsonResponse({"status": "success"})

    return HttpResponseNotFound()

def add_complaint(request):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # TODO: ngehubungin data aslinya
            rsv_id = '4235' # masi h data dummy
            cursor.execute("set search_path to sistel;")
            cursor.execute(
                """
                select email, concat(fname, ' ', lname), rhotelname, rhotelbranch
                from sistel.user, reservation_room, reservation
                where email = cust_email and rsv_id = %s and rid = rsv_id;
                """
                , (rsv_id,)
            )
            results = cursor.fetchall()
            email = results[0][0]
            nama_user = results[0][1]
            nama_hotel = results[0][2]
            cabang_hotel = results[0][3]
            context = {
                'rsv_id' : rsv_id,
                'email' : email,
                'nama_user' : nama_user,
                'nama_hotel' : nama_hotel,
                'cabang_hotel' : cabang_hotel,
            }
    return render(request, "add_complaint.html", context)

@csrf_exempt
def complaint_submit(request):
    if request.method == 'POST':
        rsv_id = request.POST.get('rsv_id')
        email = request.POST.get('email')
        deskripsi = request.POST.get('deskripsi')
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('set search_path to sistel;')
                id = 0
                cursor.execute('select id from complaints;')
                ids = cursor.fetchall()
                while (str(id),) in ids:
                    id += 1
                id = str(id)
                print(ids, id)
                query = f"""
                        insert into complaints (id,cust_email,rv_id,complaint)
                        values (%s,%s,%s,%s)
                        """
                try:
                    cursor.execute(query, (id, email, rsv_id, deskripsi))
                except Exception as e:
                    error_msg = str(e).split('\n')[0]
                    return JsonResponse({"status": "error", "message": error_msg})
        return JsonResponse({"status": "success"})

    return HttpResponseNotFound()

def add_review(request):
    # TODO: ngehubungin data aslinya
    email = 'ewinsper8@theguardian.com' # masih data dummy
    nama = 'Enid Winsper' # masih data dummy
    hotel_name = 'Ibis' # masih data dummy
    hotel_branch = 'Bandung' # masih data dummy
    context = {
        'email' : email,
        'nama' : nama,
        'hotel_name' : hotel_name,
        'hotel_branch' : hotel_branch,
    }
    return render(request, "add_review.html", context)

@csrf_exempt
def review_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nama = request.POST.get('nama')
        hotel_name = request.POST.get('hotel_name')
        hotel_branch = request.POST.get('hotel_branch')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('set search_path to sistel;')
                id = 0
                cursor.execute('select id from reviews;')
                ids = cursor.fetchall()
                while (str(id),) in ids:
                    id += 1
                id = str(id)
                print(ids, id)
                query = f"""
                        insert into reviews (cust_email, id, rating, review, hotel_name, hotel_branch)
                        values (%s,%s,%s,%s,%s,%s)
                        """
                try:
                    cursor.execute(query, (email, id, rating, review, hotel_name, hotel_branch))
                except Exception as e:
                    error_msg = str(e).split('\n')[0]
                    return JsonResponse({"status": "error", "message": error_msg})
        return JsonResponse({"status": "success"})

    return HttpResponseNotFound()