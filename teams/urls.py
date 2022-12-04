from django.contrib import admin
from django.urls import path
from teams import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.handleLogin, name="handleLogin"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('token', views.token, name="token"),
    path('faqs', views.faqs, name="faqs"),
    path('speakers', views.speakers, name="speakers"),
    path('teamsCSV', views.teamsCSV, name="teamsCSV"),
    path('verify/<auth_token>', views.verify, name="verify"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
