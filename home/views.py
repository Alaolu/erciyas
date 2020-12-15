from django.shortcuts import render, redirect
from home.models import * 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MessageForm

def home(request):
    #if request.method == "POST":
     #   formdan gelen bilgileri kaydet
     #   form = MessageForm(request.POST)
     #   if form.is_valid():
     #       form.save()
    #else:
     #    formu kullanıcıya göster
     #    form = MessageForm() 
       
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anasayfa')

    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'iletisim':Iletisim.objects.get(id=1),
        'basliklar':Maintitle.objects.get(id=1),
        'form': form,
        
    }

    return render(request, 'home.html', context)

def detay(request):
    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'basliklar':Maintitle.objects.get(id=1),
        
    }
    return render(request, 'detay.html', context)


def detay2(request):
    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'basliklar':Maintitle.objects.get(id=1),
        
    }
    return render(request, 'detay2.html', context)   


def detay3(request):
    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'basliklar':Maintitle.objects.get(id=1),
        
    }
    return render(request, 'detay3.html', context)  


def detay4(request):
    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'basliklar':Maintitle.objects.get(id=1),
        
    }
    return render(request, 'detay4.html', context)  



def bülten(request):
    bültens_list = Bülten.objects.all()
    paginator = Paginator(bültens_list, 1) #1 tane bülten gösterecek.

    page = request.GET.get('sayfa')
    try:
        bülten = paginator.page(page)
    except PageNotAnInteger:
        bülten = paginator.page(1)
    except EmptyPage:
        bülten = paginator.page(paginator.num_pages)


    context = {
        'home1':Home1.objects.get(id=1),
        'home2':Home2.objects.get(id=1),
        'home3':Home3.objects.get(id=1),
        'home4':Home4.objects.get(id=1), 
        'instagram':Instagram.objects.get(id=1),
        'twitter':Instagram.objects.get(id=2),
        'facebook':Instagram.objects.get(id=3),
        'basliklar':Maintitle.objects.get(id=1),
        'bültens':bülten,  
    }

    return render(request, 'bülten.html', context)     


