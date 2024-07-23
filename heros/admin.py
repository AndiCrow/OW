from django.contrib import admin
from .models import Tank, DamageDealer, Support, Counter, Hero

class TankAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon')
    search_fields = ('name', 'weapon')
    fields = ('name', 'weapon', 'background_story', 'first_ability', 'second_ability', 'third_ability', 'ulti')

class DamageDealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon')
    search_fields = ('name', 'weapon')
    fields = ('name', 'weapon', 'background_story', 'first_ability', 'second_ability', 'third_ability', 'ulti')

class SupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon', 'background_story')  
    search_fields = ('name', 'weapon')
    fields = ('name', 'weapon', 'background_story', 'first_ability', 'second_ability', 'third_ability', 'ulti')

admin.site.register(Tank, TankAdmin)
admin.site.register(DamageDealer, DamageDealerAdmin)
admin.site.register(Support, SupportAdmin)
admin.site.register(Counter)

