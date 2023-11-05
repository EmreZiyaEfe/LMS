from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='indexPage'),
    path('hakkimizda/',hakkimizda,name='hakkimizda'),
    path('iletisim/',iletisim,name='iletisim'),
    path('egitimlerimiz/',egitimlerimiz,name='egitimlerimiz'),
    path('sepet/',sepet,name='sepet'),
    path('dersler/',dersler,name='dersler'),
    path('egitmen/<int:egitmen_id>',egitmen,name='egitmen'),
    path('instructor/',instructor,name='instructor'),
    path('mesajlar/',mesajlar,name='mesajlar'),
    path('ogrenciLogin/',ogrenciLogin,name='ogrenciLogin'),
    path('videoPlayer/',videoPlayer,name='videoPlayer'),
    path('kursOlustur/',kursOlustur,name='kursOlustur'),
    path('videoUpload/',videoUpload,name='videoUpload')
]

