# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Crib
from .models import CribImage
from .models import Room
from .models import RoomImage
from .models import Rents
from .models import Guest
from .models import Host
from .models import Address
from .models import CribEquipments
from datetime import timedelta

# Create your views here.

#Piste mettre une variable globale pour le Crib courant
cribs = list(Crib.objects.filter(address__startswith="Av")) #list that will contain all the cribs corresponding to my preferences
crib = cribs[0]
currentCrib = -1

def browse(request):
    """
    cribs = Crib.objects.all() #Recuperer du profil de l'utilisateur
    latest_cribs = cribs.order_by('-number_of_rooms')[:5] #Ajouter système de matching ici
    context = {'latest_cribs' : latest_cribs}
    return render(request, 'cribs/browse.html', context)
    """
    #Merger Browse et nextCrib
    addresses = list(Address.objects.filter(city="Brussels"))
    global cribs
    cribs=list()
    for address in addresses:
       cribs.append(list(Crib.objects.filter(complete_address=address))[0])
    global crib
    crib = cribs.pop()
    global currentCrib
    currentCrib = crib.id

    #Recuperation du context de la page
    cribImages = CribImage.objects.filter(crib=currentCrib)
    rents = list(Rents.objects.filter(crib_id=currentCrib)) #rents for current crib
    guestsList = list()
    for rent in rents:
        if not rent.is_past_due:
            guestsList.append(Guest.objects.get(id=rent.guest_id.id))#
    host_id = crib.host.id
    host = Host.objects.get(id=host_id)
    rooms = Room.objects.filter(crib=currentCrib)
    roomImages = RoomImage.objects.filter(room=rooms)

    cribEquipments = CribEquipments.objects.filter(crib_id=currentCrib)
    print cribEquipments[0] #BUG ICI

    context = {'crib_images' : cribImages, 'crib': crib, 'guests_list': guestsList,
               'host': host, 'room_images' : roomImages, 'crib_equipments': cribEquipments}
    #
    return render(request, 'cribs/browse.html', context)

def nextCrib(request):
    #currentCrib = cribs[0].id #Freeze at the last one
    print "LENGTH CRIBS"
    print len(cribs)
    if(len(cribs)>=1):
        global crib
        crib = cribs.pop()
        global currentCrib
        currentCrib = crib.id

    #Recuperation du context de la page
    cribImages = CribImage.objects.filter(crib=currentCrib)
    rents = list(Rents.objects.filter(crib_id=currentCrib)) #rents for current crib
    guestsList = list()
    for rent in rents:
        if not rent.is_past_due:
            guestsList.append(Guest.objects.get(id=rent.guest_id.id))#
    host_id = crib.host.id
    host = Host.objects.get(id=host_id)
    rooms = Room.objects.filter(crib=currentCrib)
    roomImages = RoomImage.objects.filter(room=rooms)
    context = {'crib_images' : cribImages, 'crib': crib, 'guests_list': guestsList, 'host': host, 'room_images' : roomImages}
    #
    return render(request, 'cribs/browse.html', context)


def subscribe(request):
    form = GuestForm(request.POST or None)
    if form.is_valid():
        a=1
        #Traitement des données ici
    return render(request,'cribs/subscribe.html',locals())




def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)