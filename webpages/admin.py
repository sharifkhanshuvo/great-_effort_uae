from django.contrib import admin
from .models import HeroSlider,Service,Testimonial,About,Team,Project,Blog,Client
from django.utils.html import format_html
# Register your models here.


class AboutAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):


    # if there's already an entry, do not allow adding
        count = About.objects.all().count()
        if count == 0:


            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False


admin.site.register(HeroSlider)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(About,AboutAdmin)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Blog)

admin.site.register(Client)




