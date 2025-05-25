from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create test users in the model'

    def handle(self, *args, **kwargs):
        User = get_user_model() 
        self.stdout.write(f"Using user model: {User.__name__}") 

        user_info = [
            {
                'username': 'BigBalls',
                'first_name': 'Big',
                'last_name': 'Balls',
                'password': 'DOGE123',
                'email': 'bigballs@gmail.com'
            },
            {
                'username': 'BobSponge',
                'first_name': 'Bob',
                'last_name': 'Sponge',
                'password': 'Krusty123',
                'email': 'bobSponge@gmail.com'
            },
            {
                'username': 'JamesSong',
                'first_name': 'James',
                'last_name': 'Songs',
                'password': 'JSong234',
                'email': 'JSONG@gmail.com'
            },
            {
                'username': 'yellow',
                'first_name': 'Yellow',
                'last_name': 'Balls',
                'password': 'BallsYellow',
                'email': 'YelloBalls@gmail.com'
            },
            {
                'username': 'CR',
                'first_name': 'Crsi',
                'last_name': 'Stiano',
                'password': 'CSTIANO',
                'email': 'CrsiS@gmail.com'
            }
        ]

        for user_data in user_info:
            try:
                self.stdout.write(f"Attempting to create user: {user_data['username']}")
                
                user = User.objects.create_user(
                    username=user_data['username'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    password=user_data['password'],
                    email=user_data['email']
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created user: {user.username}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to create user {user_data["username"]}: {str(e)}')
                )

        self.stdout.write(self.style.SUCCESS('User creation completed'))