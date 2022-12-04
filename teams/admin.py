from django.contrib import admin
from .models import Team, TeamMember, FAQs

# Register your models here.
admin.site.register((Team, TeamMember, FAQs))
