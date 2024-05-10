# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('downloads/', views.downloadable_templates),
    path('signup/', views.signup),
    path('forbidden/', views.forbidden),
    path('not-found/', views.not_found),
    path('announcements/', views.get_all_announcements),
    path('get-announcement/<int:id>', views.get_announcement),
    path('add-announcement/', views.add_announcement),
    path('edit-announcement/<int:id>', views.edit_announcement),
    path('delete-announcement/<int:id>', views.delete_announcement),
    path('projects/', views.get_all_projects),
    path('get-project/<int:id>', views.get_project),
    path('add-project/', views.add_project),
    path('edit-project/<int:id>', views.edit_project),
    path('delete-project/<int:id>', views.delete_project),
    path('add-userform/', views.add_userform),
    path('delete-userform/<int:id>', views.delete_userform),
    path('get-userform/<int:id>', views.get_userform),
    path('my-forms/', views.get_my_userforms),
    path('get-pending-userforms/', views.get_pending_userforms),
    path('change-approval/<int:id>', views.change_userform_status),

]