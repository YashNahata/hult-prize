from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=100)
    leader_phone_no = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username + " | " + self.team_name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return self.team.team_name + " - " + self.first_name + " " + self.last_name
