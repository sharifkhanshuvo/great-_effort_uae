from django.contrib import admin
from .models import HeroSection, AboutSection, Service, Advantage, Work, Testimonial
from django.utils.html import format_html
# Register your models here.



class HeroSectionAdmin(admin.ModelAdmin):

    def herophoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
        count = HeroSection.objects.all().count()
        if count == 0:
            return True

        return False



    list_display = ( 'id', 'herophoto', 'title','created_date' )
    list_display_links = ( 'id', 'herophoto', 'title','created_date' )
   
class AboutSectionAdmin(admin.ModelAdmin):

    def aboutphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
        count = AboutSection.objects.all().count()
        if count == 0:
            return True

        return False



    list_display = ( 'id', 'aboutphoto', 'title','created_date' )
    list_display_links = ( 'id', 'aboutphoto', 'title','created_date' )


class ServicesAdmin(admin.ModelAdmin):

    def servicesphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    



    list_display = ( 'id', 'servicesphoto', 'title','created_date' )
    list_display_links = ( 'id', 'servicesphoto', 'title','created_date' )




class AdvantagesAdmin(admin.ModelAdmin):

    def advantagesphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    



    list_display = ( 'id', 'advantagesphoto', 'title','created_date' )
    list_display_links = ( 'id', 'advantagesphoto', 'title','created_date' )



class WorksAdmin(admin.ModelAdmin):

    def worksphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    



    list_display = ( 'id', 'worksphoto', )
    list_display_links = ( 'id', 'worksphoto', )

class TestimonialsAdmin(admin.ModelAdmin):

    def photo(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.personphoto.url))

    



    list_display = ( 'id', 'photo','personname' ,'personjobpost')
    list_display_links = ( 'id', 'photo', 'personname','personjobpost' )


admin.site.register(HeroSection,HeroSectionAdmin)
admin.site.register(AboutSection,AboutSectionAdmin)
admin.site.register(Service,ServicesAdmin)
admin.site.register(Advantage,AdvantagesAdmin)
admin.site.register(Work,WorksAdmin)
admin.site.register(Testimonial,TestimonialsAdmin)



