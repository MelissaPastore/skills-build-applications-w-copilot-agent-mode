from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Verify the test data in the database'

    def handle(self, *args, **kwargs):
        # Verify users
        users = User.objects.all()
        self.stdout.write(f"Users: {users.count()}")
        for user in users:
            self.stdout.write(f"- {user.name} ({user.email})")

        # Verify teams
        teams = Team.objects.all()
        self.stdout.write(f"Teams: {teams.count()}")
        for team in teams:
            self.stdout.write(f"- {team.name} with {team.members.count()} members")

        # Verify activities
        activities = Activity.objects.all()
        self.stdout.write(f"Activities: {activities.count()}")
        for activity in activities:
            self.stdout.write(f"- {activity.type} by {activity.user.name} for {activity.duration} minutes")

        # Verify leaderboard
        leaderboard = Leaderboard.objects.all()
        self.stdout.write(f"Leaderboard entries: {leaderboard.count()}")
        for entry in leaderboard:
            self.stdout.write(f"- {entry.team.name}: {entry.points} points")

        # Verify workouts
        workouts = Workout.objects.all()
        self.stdout.write(f"Workouts: {workouts.count()}")
        for workout in workouts:
            self.stdout.write(f"- {workout.name}: {workout.description}")