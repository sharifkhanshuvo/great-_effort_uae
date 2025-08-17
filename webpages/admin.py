from django.contrib import admin
from .models import (
    HeroSlider,
    Service,
    Testimonial,
    About,
    Team,
    Project,
    Blog,
    Client,
    ExpertWorker,
    QualityWork,
    Support,
    AboutMore,
    ContactForm,
    ExpertWorkerCount,
    ClientsCount,
    CompletedProjectCount,
    RunningProjectCount,
)

# A reusable admin that allows only a single row and disables delete
class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow "Add" only if no instance exists
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Never allow delete from admin
        return False


@admin.register(About)
class AboutAdmin(SingleInstanceAdmin):
    pass


@admin.register(AboutMore)
class AboutMoreAdmin(SingleInstanceAdmin):
    pass


@admin.register(ExpertWorker)
class ExpertWorkerAdmin(SingleInstanceAdmin):
    pass


@admin.register(QualityWork)
class QualityWorkAdmin(SingleInstanceAdmin):
    pass


@admin.register(Support)
class SupportAdmin(SingleInstanceAdmin):
    pass


@admin.register(ExpertWorkerCount)
class ExpertWorkerCountAdmin(SingleInstanceAdmin):
    pass


@admin.register(ClientsCount)
class ClientsCountAdmin(SingleInstanceAdmin):
    pass


@admin.register(CompletedProjectCount)
class CompletedProjectCountAdmin(SingleInstanceAdmin):
    pass


@admin.register(RunningProjectCount)
class RunningProjectCountAdmin(SingleInstanceAdmin):
    pass


# Regular models (no singleton logic)
admin.site.register(HeroSlider)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Client)
admin.site.register(ContactForm)
