from django.contrib import admin
from .models import *
@admin.register(Egitimler)
class EgitimlerAdmin(admin.ModelAdmin):
    list_display = ['egitimler_title',]
    prepopulated_fields = {"slug" : ("egitimler_title",),}


@admin.register(Video_player)
class Video_playerAdmin(admin.ModelAdmin):
    pass




@admin.register(Sepet)
class SepetAdmin(admin.ModelAdmin):
    pass

@admin.register(AnaCategory)
class AnaCategoryAdmin(admin.ModelAdmin):
    list_display = ['ana_category_name',]
    prepopulated_fields = {"slug" : ("ana_category_name",),}

@admin.register(AltCategory)
class AnaCategoryAdmin(admin.ModelAdmin):
    list_display = ['alt_category_name',]
    prepopulated_fields = {"slug" : ("alt_category_name",),}    

@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ['egitim_seviyesi',]    