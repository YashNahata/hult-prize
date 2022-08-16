from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=100)
    team_about = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return self.user.username + " | " + self.team_name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    linkedin_url = models.URLField(blank=True)
    def __str__(self):
        return self.team + " - " + self.first_name + " " + self.last_name
