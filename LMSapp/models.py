from django.db import models
from LMSuser.models import *
# Create your models here.


class AnaCategory(models.Model):
    ana_category_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.ana_category_name

class AltCategory(models.Model):
    alt_category_name = models.CharField(max_length=100)
    alt_category_image = models.ImageField(upload_to='category_pic')

    def __str__(self):
        return self.alt_category_name


class CourseLevel(models.Model):
    egitim_seviyesi = models.CharField(max_length=50)

    def __str__(self):
        return self.egitim_seviyesi


class Egitimler(models.Model):
    egitimler_title = models.CharField(max_length=200)
    egitim_icerigi = models.CharField(max_length=200)
    egitim_suresi = models.IntegerField()
    egitim_ana_kategori = models.ManyToManyField(AnaCategory, blank= True)
    egitim_alt_kategori = models.ForeignKey(AltCategory, on_delete= models.SET_NULL, null= True)
    egitim_image = models.ImageField(upload_to='egitim_pic')
    egitim_seviyesi = models.ForeignKey(CourseLevel,on_delete=models.SET_NULL, null=True)
    egitim_ucreti = models.IntegerField(null=True)
    egitmen = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.egitimler_title


class Video_player(models.Model):
    video_player_title = models.CharField(max_length=50)
    video_aciklama = models.TextField(max_length=300)
    video_suresi = models.IntegerField()
    media = models.URLField(max_length=800)
    video_egitmen = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    video_egitim = models.ForeignKey(Egitimler, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.video_player_title





class Sepet(models.Model):
    sepet_title = models.CharField(max_length=50)
    egitim_fiyat = models.IntegerField()
    egitim_id = models.CharField(max_length=30)
    

    def __str__(self):
        return self.sepet_title
