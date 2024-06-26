import json

import psycopg2
import psycopg2.extras
from django.conf import settings
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotAllowed, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def get_connection():
    return psycopg2.connect(
        dbname='railway',
        user='postgres',
        password='EcgcG5CGgE6b3B6B4EBaaGb-F16fddcb',
        host='viaduct.proxy.rlwy.net',
        port='57165'
    )

#testing connection in example app
conn = psycopg2.connect(dbname='railway',
                        user='postgres',
                        password='EcgcG5CGgE6b3B6B4EBaaGb-F16fddcb',
                        host='viaduct.proxy.rlwy.net',
                        port='57165',
                        )

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def daftar_kamar(request):

    query=f"""
            select * from sistel.room
            """
    cur.execute(query)
    list_kamar = cur.fetchall()
    context = {'kamars': list_kamar}

    return render(request, 'daftar_kamar.html', context)

def daftar_reservasi(request):

    query=f"""
            SELECT r.rid, rr.datetime, rr.rnum, rs.status
            FROM sistel.reservation as r
            JOIN sistel.reservation_room as rr on r.rid = rr.rsv_id
            JOIN sistel.reservation_status_history as rsh on r.rid = rsh.rid 
            JOIN sistel.reservation_status as rs on rsh.rsid = rs.id
            where r.cust_email = %s
            """
    cur.execute(query, (request.session['user'],))
    list_reservasi = cur.fetchall()
    context = {'reservasis': list_reservasi}

    return render(request, 'daftar_reservasi.html', context)

def create_kamar(request):

    query=f"""
            SELECT *
            FROM sistel.room
            """
    cur.execute(query)
    detail_kamar = cur.fetchall()
    context = {'detail_kamar': detail_kamar}
    print(detail_kamar) #checker

    return render(request, 'create_kamar.html', context)

def detail_reservasi(request, rsv_id):

    query=f"""
            SELECT rsv_id, rnum, rhotelname, rhotelbranch, datetime, isactive
            FROM sistel.reservation_room
            where rsv_id = %s
            """
    cur.execute(query, (rsv_id, ))
    detail_reservasi = cur.fetchone()
    query=f"""
        SELECT rsv_id, vehicle_num, driver_phonenum, datetime, isactive
        FROM sistel.reservation_shuttleservice
        where rsv_id = %s and isactive = true;
        """
    cur.execute(query, (rsv_id, ))
    detail_shuttle = cur.fetchone()
    context = {'detail_reservasi': detail_reservasi, 'detail_shuttle':detail_shuttle, 'rsv_id' : rsv_id}
    print(detail_reservasi) #checker

    return render(request, 'detail_reservasi.html', context)
