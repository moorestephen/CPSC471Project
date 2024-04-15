from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_page, name = 'login'),
    # path('swimmer-dashboard/', views.swimmer_dashboard, name = 'swimmer_dashboard'),
    # path('coach-dashboard/', views.coach_dashboard, name = 'coach_dashboard'),
    # path('admin-dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('clubs/', views.ClubListCreate.as_view()),
    path('swimmers-and-group/', views.SwimmerAndGroupList.as_view()),
    path('coaches-and-group/', views.CoachAndGroupList.as_view()),
    path('swimmers/', views.SwimmerListCreate.as_view()),
    # path('upcoming_competitions/', views.UpcomingCompetitionList.as_view()),
    path('event_record/', views.EventRecordListCreate.as_view()),
    path('group-names/', views.GroupNameOnlyList.as_view()),
    path('event_record/', views.EventRecordListCreate.as_view()),
    path('swimmers/', views.SwimmerListCreate.as_view()),
    path('coaches/', views.CoachListCreate.as_view()),
    path('group-coach', views.GroupCoachesListCreate.as_view()),
    path('upcoming_competitions/', views.UpcomingCompetitionListCreate.as_view()),
    path('event_record/', views.EventRecordListCreate.as_view()),
    path('swimmers-group/', views.SwimmerGroupListCreate.as_view()),
    path('groups/', views.GroupListCreate.as_view()),
    path('create-user/', views.UserListCreate.as_view()),
    path('retrieve-user/', views.UserLogin.as_view()),
    path('competitions/', views.CompetitionListCreate.as_view()),
    path('competitionNames/', views.CompetitionNameOnlyList.as_view())
]