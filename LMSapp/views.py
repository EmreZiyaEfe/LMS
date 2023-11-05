from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

def hakkimizda(request):
    return render(request,'hakkimizda.html')

def iletisim(request):
    return render(request,'iletisim.html')

def egitimlerimiz(request):
    anacategory = AnaCategory.objects.all()
    altcategory = AltCategory.objects.all() 
    return render(request,'egitimlerimiz.html', {'anacategory': anacategory, 'altcategory' : altcategory})

def sepet(request):
    return render(request,'sepet.html')

def dersler(request):
    dersler = Egitimler.objects.all()
    return render(request,'dersler.html',{'dersler':dersler})

def egitmen(request, egitmen_id):
    dersler = Egitimler.objects.filter(egitmen_id = egitmen_id)
    context = {
        'dersler' : dersler
    }
    return render(request,'egitmen.html', context)

def instructor(request):
    return render(request,'instructor.html')

def mesajlar(request):
    return render(request,'mesajlar.html')

def ogrenciLogin(request):
    return render(request,'ogrenciLogin.html')

def videoPlayer(request):
    videolar = Video_player.objects.all()
    context = {
        'videolar':videolar
    }
    return render(request,'videoPlayer.html', context)

@login_required(login_url='login')
def kursOlustur(request):
        if request.user.is_teacher == True:
            if request.method == 'POST':
                courseForm = CreateCourseForm(request.POST, request.FILES)
                if courseForm.is_valid():
                    new_course = Egitimler(
                        egitimler_title = courseForm.cleaned_data['egitimler_title'],
                        egitim_icerigi = courseForm.cleaned_data['egitim_icerigi'],
                        egitim_alt_kategori =courseForm.cleaned_data['egitim_alt_kategori'],
                        egitim_seviyesi = courseForm.cleaned_data['egitim_seviyesi'],
                        egitim_suresi = courseForm.cleaned_data['egitim_suresi'],
                        egitim_ucreti = courseForm.cleaned_data['egitim_ucreti'],
                        egitim_image = courseForm.cleaned_data['egitim_image'],
                        egitmen = request.user
                    )

                    new_course.save()

                    for kategori in courseForm.cleaned_data['egitim_ana_kategori']:
                        new_course.egitim_ana_kategori.add(kategori)

                    messages.success(request, 'Kurs oluşturuldu')
                
                else:
                    print(courseForm.errors) 

                    return redirect('indexPage')
            else:
                courseForm = CreateCourseForm()

        else: 
            messages.error(request, 'Kurs oluşturmak için yetkili değilsiniz.')

            return redirect('indexPage')
        
        context = {
            'courseForm':courseForm
        }
        return render(request, 'kursOlustur.html', context)

@login_required(login_url='login')
def videoUpload(request):
    if request.user.is_teacher == True:
        if request.method == 'POST':
            videoForm = CreateVideoForm(request.POST)
            if videoForm.is_valid():
                new_video = Video_player(
                    video_player_title = videoForm.cleaned_data['video_player_title'],
                    video_aciklama = videoForm.cleaned_data['video_aciklama'],
                    video_suresi = videoForm.cleaned_data['video_suresi'],
                    video_id = videoForm.cleaned_data['video_id'],
                    video_egitim = videoForm.cleaned_data['video_egitim'],
                )

                new_video.save()

                return redirect('indexPage')
        else:
            videoForm = CreateVideoForm()

    else:     
        messages.error(request, 'Video yüklemek için yetkili değilsiniz.')

        return redirect('indexPage')
        
    context = {
        'videoForm':videoForm
    }

    return render(request,'videoUpload.html', context)
