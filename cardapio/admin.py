from django.contrib import admin
from .models import Prato


class ListandoPratos(admin.ModelAdmin):
    list_display = ('id', 'nome_prato', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_prato')
    search_fields = ('nome_prato',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Prato, ListandoPratos)
