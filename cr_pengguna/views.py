from django.db import connection as conn
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        if role == 'customer':
            return redirect('cr_pengguna:register_user')

        elif role == 'hotel':
            return redirect('cr_pengguna:register_hotel')
            pass

        return HttpResponse(f'Registration successful for {role}')

    return render(request, 'form.html')

@csrf_exempt
def register_user(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        fname = request.POST.get('FirstName')
        lname = request.POST.get('LastName')
        phonenum = request.POST.get('PhoneNumber')
        nik = request.POST.get('NIK')
        with conn.cursor() as cursor:
            cursor.execute('select email from sistel.user where email = %s', (email, ))
            res = cursor.fetchone()
            if res:
                msg = 'Email sudah terdaftar!'
            else:
                try:
                    cursor.execute('insert into sistel.user(email, password, fname, lname) values(%s,%s,%s,%s)',(email,password,fname,lname))
                    cursor.execute('insert into sistel.reservation_actor(email, phonenum, admin_email) values(%s,%s,\'tfigiovanni0@zdnet.com\')',(email,phonenum))
                    cursor.execute('insert into sistel.customer(email, nik) values(%s,%s)',(email,nik))
                except Exception as e:
                    msg = str(e).split('\n')[0]
            
        if not msg:
            return redirect('login:login')
    return render(request, 'register_user.html', {'message':msg})

@csrf_exempt
def register_hotel(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        owner_first_name = request.POST.get('OwnerFirstName')
        owner_last_name = request.POST.get('OwnerLastName')
        owner_phone_number = request.POST.get('OwnerPhoneNumber')
        business_license_number = request.POST.get('BusinessLicenseNumber')
        hotel_name = request.POST.get('HotelName')
        hotel_branch = request.POST.get('HotelBranch')
        hotel_street = request.POST.get('HotelStreet')
        hotel_district = request.POST.get('HotelDistrict')
        hotel_city = request.POST.get('HotelCity')
        hotel_province = request.POST.get('HotelProvince')

        with conn.cursor() as cursor:
            cursor.execute('select email from sistel.user where email = %s', (email, ))
            res = cursor.fetchone()
            if res:
                msg = 'Email sudah terdaftar!'
            else:
                try:
                    cursor.execute('insert into sistel.user(email, password, fname, lname) values(%s,%s,%s,%s)',(email,password,owner_first_name,owner_last_name))
                    cursor.execute('insert into sistel.reservation_actor(email, phonenum, admin_email) values(%s,%s,\'tfigiovanni0@zdnet.com\')',(email,owner_phone_number))
                    cursor.execute("""insert into sistel.hotel(
                                    email,
                                    hotel_name,
                                    hotel_branch,
                                    nib,
                                    star,
                                    street,
                                    district,
                                    city,
                                    province,
                                    description
                                ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (email, hotel_name, hotel_branch, business_license_number, 5, hotel_street, hotel_district, hotel_city, hotel_province, '',))
                except Exception as e:
                    msg = str(e).split('\n')[0]
            
        if not msg:
            return redirect('login:login')
    return render(request, 'register_hotel.html', {'message':msg})
