from django.shortcuts import render, redirect
from vinotecaperdi.addwine.forms import AddWineForm
from vinotecaperdi.addwine.models import Wine, Rate
from django.contrib.auth.decorators import login_required
from vinotecaperdi.addwine.forms import VoteWineForm
from django.db.models import Avg

import numpy as np

@login_required
def thanks(request):
    return render(request, 'thanks.html')

@login_required
def addnewwine(request):
    if request.method == 'POST':
        form = AddWineForm(request.POST)
        print request.POST
        if form.is_valid():
            wine = Wine()
            #wine = form.save(commit=False)
            wine.name_wine = request.POST.get('name_wine')
            wine.winery = request.POST.get('winery')
            wine.harvest = request.POST.get('harvest')
            wine.varietal = request.POST.get('varietal')
            wine.user_name = request.user.username
            wine.save()
            return redirect('thanks')
    else:
        form = AddWineForm()
    return render(request, 'form_addwine.html', {'form': form})

def listwineuser(request):
    username = request.user.username
    model = Wine
    queryset = Wine.objects.filter(user_name=username)
    context={
        "object_list": queryset
    }
    return render(request, 'mywines.html', context)

def WineListView(request):
    model = Wine
    queryset = Wine.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'votes.html', context)

def RateWine(request):
    if request.method == 'POST':
        form = VoteWineForm(request.POST)
        if form.is_valid():
            rate = Rate()
            rate.name_wine = request.POST.get('name_wine')
            rate.rate = request.POST.get('rate')
            rate.save()
            return redirect('home')
    else:
        form = VoteWineForm()
    return render(request, 'votes.html', {'form': form})

def ranking(request):
    ranking_list = []
    for wine in Wine.objects.all():
        list_rate = Rate.objects.filter(name_wine=wine.name_wine).order_by('-rate').aggregate(Avg('rate'))
        
        if None is not list_rate.get('rate__avg'):
            avg_rate = round(list_rate.get("rate__avg"))
            ranking_list.append((wine.name_wine, avg_rate))
    context = {"object_list": ranking_list}
    return render(request, 'ranking.html', context)
