from django.contrib import admin
from .models import HeroSlider,Service,Testimonial
from django.utils.html import format_html
# Register your models here.




   
admin.site.register(HeroSlider)
admin.site.register(Service)
admin.site.register(Testimonial)




