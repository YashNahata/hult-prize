from django.contrib import admin
from .models import Team, TeamMember, Faq, Speaker, UnverifiedTeamMember, SpeakersFaq

# Register your models here.
admin.site.register((Team, TeamMember, Faq, Speaker, UnverifiedTeamMember, SpeakersFaq))
