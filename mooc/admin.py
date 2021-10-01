from django.contrib import admin
from mooc.models import Contact,Confession,Image
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Insta','Comments')
admin.site.register(Contact,ContactAdmin)
admin.site.register(Confession)
admin.site.register(Image)
