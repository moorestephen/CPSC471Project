#from django.contrib.auth.decorators import login_required, permission_required
#from django.shortcuts import render

# def login_page(request):
#     return HttpResponse("<h1>Login Page<h1>")

# def swimmer_dashboard(request):
#     #Swimmer-specific view logic
#     return HttpResponse("<h1>Swimmer Dashboard<h1>")

# def coach_dashboard(request):
#     #Coach-specific view logic
#     return HttpResponse("<h1>Coach Dashboard<h1>")

# def admin_dashboard(request):
#     #Admin-specific view logic
#     return HttpResponse("<h1>Admin Dashboard<h1>")

from django.db import connection
from .models2 import (DatabaseClub, DatabaseAdmin, DatabaseCoach, DatabaseCompetition,
                      DatabaseCompetitioncoachdelegations, DatabaseCompetitionswimmersattending,
                      DatabaseEntry, DatabaseEvent, DatabaseEventrecord, DatabaseGroup, DatabaseGroupcoaches,
                      DatabaseGrouppractices, DatabaseSwimmer, DatabaseSwimmergroup)
from .serializers import (ClubListSerializer, DatabaseAdminSerializer, DatabaseCoachSerializer,
                          DatabaseCompetitionSerializer, DatabaseCompetitioncoachdelegationsSerializer,
                          DatabaseCompetitionswimmersattendingSerializer, DatabaseEntrySerializer,
                          DatabaseEventSerializer, DatabaseEventrecordSerializer, DatabaseGroupSerializer,
                          DatabaseGroupcoachesSerializer, DatabaseGrouppracticesSerializer, DatabaseSwimmerSerializer,
                          DatabaseSwimmergroupSerializer, SwimmerAndGroupSerializer)
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
    
class ClubList(generics.ListCreateAPIView):
    queryset = DatabaseClub.objects.all()
    serializer_class = ClubListSerializer

class AdminList(generics.ListCreateAPIView):
    queryset = DatabaseAdmin.objects.all()
    serializer_class = DatabaseAdminSerializer 

class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseAdmin.objects.all()
    serializer_class = DatabaseAdminSerializer

class CoachList(generics.ListCreateAPIView):
    queryset = DatabaseCoach.objects.all()
    serializer_class = DatabaseCoachSerializer

class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseCoach.objects.all()
    serializer_class = DatabaseCoachSerializer

class CompetitionList(generics.ListCreateAPIView):
    queryset = DatabaseCompetition.objects.all()
    serializer_class = DatabaseCompetitionSerializer

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseCompetition.objects.all()
    serializer_class = DatabaseCompetitionSerializer

class CompetitionCoachDelegationsList(generics.ListCreateAPIView):
    queryset = DatabaseCompetitioncoachdelegations.objects.all()
    serializer_class = DatabaseCompetitioncoachdelegationsSerializer

class CompetitionCoachDelegationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseCompetitioncoachdelegations.objects.all()
    serializer_class = DatabaseCompetitioncoachdelegationsSerializer

class CompetitionSwimmersAttendingList(generics.ListCreateAPIView):
    queryset = DatabaseCompetitionswimmersattending.objects.all()
    serializer_class = DatabaseCompetitionswimmersattendingSerializer

class CompetitionSwimmersAttendingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseCompetitionswimmersattending.objects.all()
    serializer_class = DatabaseCompetitionswimmersattendingSerializer

class EntryList(generics.ListCreateAPIView):
    queryset = DatabaseEntry.objects.all()
    serializer_class = DatabaseEntrySerializer

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseEntry.objects.all()
    serializer_class = DatabaseEntrySerializer

class EventList(generics.ListCreateAPIView):
    queryset = DatabaseEvent.objects.all()
    serializer_class = DatabaseEventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseEvent.objects.all()
    serializer_class = DatabaseEventSerializer

class EventRecordList(generics.ListCreateAPIView):
    queryset = DatabaseEventrecord.objects.all()
    serializer_class = DatabaseEventrecordSerializer

class EventRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseEventrecord.objects.all()
    serializer_class = DatabaseEventrecordSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = DatabaseGroup.objects.all()
    serializer_class = DatabaseGroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseGroup.objects.all()
    serializer_class = DatabaseGroupSerializer

class GroupCoachesList(generics.ListCreateAPIView):
    queryset = DatabaseGroupcoaches.objects.all()
    serializer_class = DatabaseGroupcoachesSerializer

class GroupCoachesDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = DatabaseGroupcoaches.objects.all()
    serializer_class = DatabaseGroupcoachesSerializer

class GroupPracticesList(generics.ListCreateAPIView):
    queryset = DatabaseGrouppractices.objects.all()
    serializer_class = DatabaseGrouppracticesSerializer

class GroupPracticesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseGrouppractices.objects.all()
    serializer_class = DatabaseGrouppracticesSerializer

class SwimmerList(generics.ListCreateAPIView):
    queryset = DatabaseSwimmer.objects.all()
    serializer_class = DatabaseSwimmerSerializer

class SwimmerAndGroupList(APIView):
    def get(self, request):
        queryset = DatabaseSwimmer.objects.raw(
            'SELECT 1 AS id, email, fname, lname, dob, group_id FROM database_swimmer INNER JOIN database_swimmergroup ON database_swimmer.email = database_swimmergroup.swimmer_id'
        )
        serialized = SwimmerAndGroupSerializer(queryset, many=True)
        return Response(serialized.data)
    
class UpcomingCompetitionList(APIView):
    def get(self, request, format=None):
        queryset = DatabaseCompetition.objects.raw(
            "SELECT * FROM database_competition WHERE end_date >= date('now')"
        )
        serialized = DatabaseCompetitionSerializer(queryset, many=True)
        return Response(serialized.data)

class SwimmerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseSwimmer.objects.all()
    serializer_class = DatabaseSwimmerSerializer

class SwimmerGroupList(generics.ListCreateAPIView):
    queryset = DatabaseSwimmergroup.objects.all()
    serializer_class = DatabaseSwimmergroupSerializer

class SwimmerGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatabaseSwimmergroup.objects.all()
    serializer_class = DatabaseSwimmergroupSerializer