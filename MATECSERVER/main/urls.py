# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
    path('forbidden/', views.forbidden),
    path('not-found/', views.not_found),
    path('announcements/', views.get_all_announcement),
    path('get-announcement/<int:id>', views.get_announcement),
    path('add-announcement/', views.add_announcement),
    path('edit-announcement/<int:id>', views.edit_announcement),
    path('delete-announcement/<int:id>', views.delete_announcement),
]