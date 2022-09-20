from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    count_watched = MyWatchlist.objects.filter(watched = True).count()
    count_unwatched = MyWatchlist.objects.filter(watched = False).count()

    if (count_watched) >= count_unwatched:
        display_text = "Selamat, kamu sudah banyak menonton!"
    else:
        display_text = "Wah, kamu masih sedikit menonton!"

    context = {
        'movie_list': MyWatchlist.objects.all(),
        'name_id': "Alanna (2106639913)",
        'display_text': display_text,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")  

def show_json_by_id(request,id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")   

    