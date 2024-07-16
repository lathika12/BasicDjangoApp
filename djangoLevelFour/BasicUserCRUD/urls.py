from django.urls import path, include
from BasicUserCRUD import views

app_name = 'BasicUserCRUD'

urlpatterns = [
    path('', views.index, name='index'),
    path('userprofile', views.users_profile, name='userprofile'),
    path('allusers', views.view_user_data, name='allusers'),
]