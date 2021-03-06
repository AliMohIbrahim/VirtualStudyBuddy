from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

appname = "virtualstudybuddy"
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls), #admin
    path('accounts/', include('allauth.urls')), #google login
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout_view, name= "logout"),
    
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'), #profile page
    path('editProfile/', views.editProfile, name = "editProfile"),
    path('viewProfiles/', views.get_profiles, name="viewProfiles"),
    path('viewProfiles/redirect/<int:pk>/', views.ProfileView.as_view(), name='profile'),  # probably don't need this anymore
    
    path('match/<int:pk>', views.manual_match, name="manualMatch"),
    
    path('mygroups/', views.my_groups, name="mygroups"),
    path('allgroups/', views.all_groups, name="allgroups"),
    path('group/<int:pk>/', views.group_page, name='group'), 
    path('creategroup/', views.creategroup, name = "creategroup"),
    path('editgroup/<int:pk>/', views.editgroup, name="editgroup"),
    path('leavegroup/<int:pk>/', views.leavegroup, name="leavegroup"),
    path('meetgroup/<int:pk>/', views.meetgroup, name="meetgroup"),
    path('joingroup/<int:pk>', views.join_group, name="joingroup"),

    path('inbox/', views.my_inbox, name="myinbox"),
    path('composemessage/', views.compose_message, name="composemessage"),
    path('composemessage/<str:target>', views.compose_message, name="composemessage"),
    path('deletemessage/<int:pk>', views.delete_message, name="deletemessage"),

    path('chat/', views.chatindex, name='chatindex'),
    path('chat/<str:room_name>/', views.room, name='room'),
] 
