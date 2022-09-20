from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    context = {
        'movie_list': MyWatchlist.objects.all(),
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

    