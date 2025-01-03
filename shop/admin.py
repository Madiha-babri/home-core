from django.contrib import admin
from .models import Shop
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Shop)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

   
