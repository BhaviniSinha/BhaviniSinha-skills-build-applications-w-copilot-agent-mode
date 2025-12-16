from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, UserViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('v1/', include(router.urls)),
]
