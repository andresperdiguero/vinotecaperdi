from django.shortcuts import render, redirect
from vinotecaperdi.addwine.forms import AddWineForm
from vinotecaperdi.addwine.models import Wine
from django.contrib.auth.decorators import login_required

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
            return redirect('home')
    else:
        form = AddWineForm()
    return render(request, 'form_addwine.html', {'form': form})



def listwine(request):
    username = request.user.username
    model = Wine
    queryset = Wine.objects.filter(user_name=username)
    context={
        "object_list": queryset
    }
    return render(request, 'mywines.html', context)
