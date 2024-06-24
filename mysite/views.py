from django.shortcuts import render # Untuk memanggil file html
from django.http import HttpRequest # Format html langsung di tulis didalam HttpRequest
from berita.models import Artikel,Kategori

def home (request):
    templates_name = 'halaman/index.html'
    kategori = request.GET.get('kategori')
    if kategori == None:
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        print("Bukan ALL")
        get_kategori = Kategori.objects.filter(nama=kategori)
        print(get_kategori)
        if  get_kategori.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=get_kategori[0])
            menu_aktif = kategori

        else:
            menu_aktif = "ALL"
            data_artikel = []


    data_kategori = Kategori.objects.all()
    print(data_artikel)
    context = {
        'title' : 'Selamat Datang :)',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori,
        'menu_aktif' : menu_aktif,
    }
    return render(request, templates_name, context)

def about(request):
    templates_name = "halaman/about.html"
    context = {
        'title' : 'about ',
        'welcome' : 'ini page about',
    }
    return render(request, templates_name,context)

def contact(request):
    templates_name = 'halaman/contact.html'
    context = {
        'title' : 'contact',
        'welcome' : 'ini page about',
    }
    return render(request, templates_name,context)

def detail_artikel(request, id):
    templates_name = 'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(id=id)
    print(artikel)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel,
    } 
    return render(request, templates_name,context)