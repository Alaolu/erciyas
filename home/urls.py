from django.urls import path
from home.views import home
from home.views import detay
from home.views import detay2
from home.views import detay3
from home.views import detay4
from home.views import bülten
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', home, name='anasayfa'),
    path('detay/', detay, name='detay'),
    path('detay2/', detay2, name='detay2'),
    path('detay3/', detay3, name='detay3'),
    path('detay4/', detay4, name='detay4'),
    path('bülten/', bülten, name='bülten'),

]