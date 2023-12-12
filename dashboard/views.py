from django.db import connection as conn
from django.shortcuts import render

# Create your views here.

def show_dashboard(request):
    if 'hotel_name' in request.session:
        email = request.session['user']
        with conn.cursor() as cursor:
            cursor.execute("""select concat(fname,' ',lname),phonenum,nib, hotel_name, hotel_branch, concat(street, ', ', district, ', ', city, ', ', province) from sistel.user U,sistel.reservation_actor R,sistel.hotel H
                            where U.email = %s and R.email = %s and H.email = %s;
                            """, (email, email, email))
            res = cursor.fetchone()
            cursor.execute('select facility_name from sistel.hotel_facilities where hotel_name = %s and hotel_branch = %s;', (res[3], res[4]))
            response = cursor.fetchall()
            cursor.execute("""select r.number, r.price, r.floor, string_agg(distinct f.id, \', \')
                            from sistel.room r, sistel.room_facilities f
                            where r.hotel_name = %s and r.hotel_branch = %s and f.rnum = r.number and r.hotel_name = f.hotel_name and r.hotel_branch = f.hotel_branch
                            group by r.number, r.hotel_name, r.hotel_branch;
                            """, (res[3], res[4]))
            room = cursor.fetchall()
            for i in range(len(response)):
                response[i] = response[i][0]
            context = {
                'nama' : res[0],
                'phonenum' : res[1],
                'email' : email,
                'nib' : res[2],
                'nama_hotel' : res[3] + ' - ' + res[4],
                'alamat' : res[5],
                'response' : response,
                'rooms' : room,
            }
        print(res)
        return render(request, 'dash_hotel.html', context)
    else:
        email = request.session['user']
        with conn.cursor() as cursor:
            cursor.execute("""select fname,lname,phonenum,nik from sistel.user U,sistel.reservation_actor R,sistel.customer C
                            where U.email = %s and R.email = %s and C.email = %s;
                            """, (email, email, email))
            res = cursor.fetchone()
            context = {
                'fname' : res[0],
                'lname' : res[1],
                'pnum' : res[2],
                'email' : email,
                'nik' : res[3],
            }
        print(res)
        return render(request, 'dash_user.html', context)
