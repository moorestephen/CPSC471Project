from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_page, name = 'login'),
    # path('swimmer-dashboard/', views.swimmer_dashboard, name = 'swimmer_dashboard'),
    # path('coach-dashboard/', views.coach_dashboard, name = 'coach_dashboard'),
    # path('admin-dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('clubs/', views.ClubList.as_view()),
    path('swimmers-and-group/', views.SwimmerAndGroupList.as_view()),
    path('swimmers/', views.SwimmerList.as_view()),
    path('groups/', views.GroupNameOnlyList.as_view()),
]
