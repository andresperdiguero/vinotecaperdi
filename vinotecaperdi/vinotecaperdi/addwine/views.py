from django.shortcuts import render, redirect
from vinotecaperdi.addwine.forms import AddWineForm
from vinotecaperdi.addwine.models import Wine, Rate
from django.contrib.auth.decorators import login_required
from vinotecaperdi.addwine.forms import VoteWineForm

@login_required
def thanks(request):
    return render(request, 'thanks.html')

@login_required
def addnewwine(request):
    if request.method == 'POST':
        form = AddWineForm(request.POST)
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
            rate.wine_name = request.POST.get('wine')
            rate.rank = request.POST.get('rank')
            form.save()
    return render(request, 'home.html', {'form': form})
