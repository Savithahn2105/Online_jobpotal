from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from jobs import views as jobs_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('register/', jobs_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='jobs/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='jobs/logout.html'), name='logout'),

    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)