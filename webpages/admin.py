from django.contrib import admin
from .models import HeroSlider,Service,Testimonial,About,Team,Project,Blog,Client,ExpertWorker,QualityWork,Support,AboutMore,ContactForm,ExpertWorkerCount,ClientsCount,CompletedProjectCount,RunningProjectCount
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



class AboutMoreAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = AboutMore.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):
        

        return False


class ExpertWorkerAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = ExpertWorker.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False

class QualityWorkAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = QualityWork.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False



class SupportAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = Support.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False


class ExpertWorkerCountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = ExpertWorkerCount.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False

class ClientsCountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = ClientsCount.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False


class CompletedProjectCountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = CompletedProjectCount.objects.all().count()
        if count == 0:



            return True

        return False

    def has_delete_permission(self, request,obj=None):

        return False

class RunningProjectCountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):



    # if there's already an entry, do not allow adding
        count = RunningProjectCount.objects.all().count()
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
admin.site.register(ExpertWorker,ExpertWorkerAdmin)
admin.site.register(QualityWork,QualityWorkAdmin)
admin.site.register(Support,SupportAdmin)
admin.site.register(AboutMore,AboutMoreAdmin)
admin.site.register(ContactForm)
admin.site.register(ExpertWorkerCount,ExpertWorkerCountAdmin)
admin.site.register(ClientsCount,ClientsCountAdmin)
admin.site.register(CompletedProjectCount,CompletedProjectCountAdmin)
admin.site.register(RunningProjectCount,RunningProjectCountAdmin)







