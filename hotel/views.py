from collections import namedtuple

from django.contrib import messages
from django.db import IntegrityError, connection
from django.db.utils import InternalError
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


def namedtuplefetchall(cursor):
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def fasilitas_hotel(request, hotel_name:str, hotel_branch:str):
    hotel_name = hotel_name.title()
    hotel_branch = hotel_branch.title()
    with connection.cursor() as c:
        c.execute("""set search_path to sistel""")
        c.execute(f"""
        select *
        from hotel_facilities
        where hotel_name = '{hotel_name}' and hotel_branch = '{hotel_branch}'
        """)
        response = namedtuplefetchall(c)

        hotel_branch = response[0][1]
        c.execute("""set search_path to public""")
        return render(request, "fasilitas.html", {"response":response, "hotel_brach":hotel_branch})

# Create your views here.
def find_hotel(request):
    return render(request, "search_hotel.html", {})

def specific_hotel(request):
    return render(request, "specific_hotel.html", {})


def create_fasilitas_hotel(request, hotel_name: str, hotel_branch:str):
    if request.method == "POST":

            facility = request.POST.get('facility_name')

            try :
                hotel_name = hotel_name.title()
                hotel_branch = hotel_branch.title()
                with connection.cursor() as c:
                    c.execute("set search_path to sistel")
                    c.execute(f"""
                    INSERT INTO hotel_facilities(hotel_name, hotel_branch, facility_name)
                    VALUES ('{hotel_name}', '{hotel_branch}', '{facility}')
                    """)
                    c.execute("""set search_path to public""")
                return redirect(f'/hotel/fasilitas/{hotel_name}/{hotel_branch}')
            except Exception as e:
                print(e)
                return render(request, "create_fasilitas.html", {"message" : str(e).split('\n')[0]})

    return render(request, "create_fasilitas.html", {})



def update_fasilitas_hotel(request, hotel_name, hotel_branch, facilities):
    hotel_name = hotel_name.title()
    hotel_branch = hotel_branch.title()
    if request.method == "POST":

            facility = request.POST.get('facility_name')

            try : 
                with connection.cursor() as c:
                    c.execute("set search_path to sistel")
                    c.execute(f"""
                    update hotel_facilities
                    set facility_name = '{facility}'
                    where hotel_name = '{hotel_name}' and hotel_branch = '{hotel_branch}' and facility_name = '{facilities}'
                    """)
                    c.execute("""set search_path to public""")
                return redirect(f'/hotel/fasilitas/{hotel_name}/{hotel_branch}')
        
            except Exception as e:
                with connection.cursor() as c:
                    c.execute("""set search_path to sistel""")
                    c.execute(f"""
                    select *
                    from hotel_facilities
                    where hotel_name = '{hotel_name}' and hotel_branch = '{hotel_branch}' and facility_name = '{facilities}'
                    """)
                    response = namedtuplefetchall(c)
                    facility_temp = facilities
                    c.execute("""set search_path to public""")
                return render(request, "update_fasilitas.html", {"response" : response, "facility":facility_temp, "message" : str(e).split('\n')[0]})
            
            
    with connection.cursor() as c:
        c.execute("""set search_path to sistel""")
        c.execute(f"""
        select *
        from hotel_facilities
        where hotel_name = '{hotel_name}' and hotel_branch = '{hotel_branch}' and facility_name = '{facilities}'
        """)
        response = namedtuplefetchall(c)
        facility_temp = facilities
        c.execute("""set search_path to public""")
    return render(request, "update_fasilitas.html", {"response" : response, "facility":facility_temp})
    

def delete_fasilitas_hotel(request, hotel_name, hotel_branch, facilities):
    hotel_branch = hotel_branch.title()
    hotel_name = hotel_name.title()
            
    with connection.cursor() as c:
        c.execute("""set search_path to sistel""")
        c.execute(f"""
        delete from hotel_facilities
        where hotel_name = '{hotel_name}' and hotel_branch = '{hotel_branch}' and facility_name = '{facilities}'
        """)
        c.execute("""set search_path to public""")
        return redirect(f'/hotel/fasilitas/{hotel_name}/{hotel_branch}')

    