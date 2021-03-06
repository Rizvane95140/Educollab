"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from account.views import (
    registration_view,
    login_view,
    home_account,
    infos,
    discussion,
    exercer,
    corriger,
    evaluation,
    correction_prof,
    modification,
    add_exo,
    add_ctrl,
    logout_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registration_view, name="register"),
    path('', login_view, name="login"),
    path('home/',home_account, name="home" ),
    path('infos/',infos, name="infos" ),
    path('discussion/',discussion, name="discussion" ),
    path('exercer/',exercer, name="exercer" ),
    path('corriger/',corriger, name="corriger" ),
    path('evaluation/',evaluation, name="evaluation" ),
    path('correction_prof/',correction_prof, name="correction_prof" ),
    path('modification/',modification, name="modification" ),
    path('add_exo/',add_exo, name="add_exo" ),
    path('add_ctrl/',add_ctrl, name="add_ctrl" ),
    path('logout/', logout_view, name="logout"),

    # Mot de passe oublié. 
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)