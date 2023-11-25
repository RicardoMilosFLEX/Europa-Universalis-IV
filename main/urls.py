from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('forum', views.forum, name='forum'),
    path('forumnote', views.createnote, name='forumnote'),
    path('registration', views.registration, name = 'registration')
]
