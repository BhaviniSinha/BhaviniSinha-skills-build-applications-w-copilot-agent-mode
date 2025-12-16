from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class SimpleModelTests(TestCase):
    def test_create_team_user_activity(self):
        t = Team.objects.create(name='Test')
        u = User.objects.create(email='a@test.com', name='Tester', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
