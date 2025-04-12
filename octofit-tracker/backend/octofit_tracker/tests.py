from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password123')
        activity = Activity.objects.create(user=user, activity_type='Running', duration='01:00:00')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        team = Team.objects.create(name='Test Team')
        leaderboard_entry = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(leaderboard_entry.total_points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Run', description='A quick morning run', duration='00:30:00', calories_burned=300)
        self.assertEqual(workout.name, 'Morning Run')
