from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import lorem_text
from Notes.models import Notes
from lorem_text import lorem

User = get_user_model()

class Command(BaseCommand):
    help = "Creating the notes"

    def handle(self, *args, **kwargs):
        note_samples = [
            {
                'idx':1,
                'name':lorem.words(9),
                'description':lorem.sentence(),
                'status':'Simple',
                'author':User.objects.get(username='BigBalls')
            },

            {
                'idx':2,
                'name':lorem.words(6),
                'description':lorem.sentence(),
                'status':'Urge',
                'author':User.objects.get(username='CR')
            },

            {
                'idx':3,
                'name':lorem.words(5),
                'description':lorem.sentence(),
                'status':'Deadline',
                'author':User.objects.get(username='JamesSong')
            },

            {
                'idx':4,
                'name':lorem.words(2),
                'description':lorem.sentence(),
                'status':'Urge',
                'author':User.objects.get(username='yellow')
            },

            {
                'idx':5,
                'name':lorem.words(7),
                'description':lorem.sentence(),
                'status':'Deadline',
                'author':User.objects.get(username='BobSponge')
            },

            {
                'idx':6,
                'name':lorem.words(10),
                'description':lorem.sentence(),
                'status':'Simple',
                'author':User.objects.get(username='CR')
            },

            {
                'idx':7,
                'name':lorem.words(1),
                'description':lorem.sentence(),
                'status':'Urge',
                'author':User.objects.get(username='yellow')
            },
            
            {
                'idx':8,
                'name':lorem.words(8),
                'description':lorem.sentence(),
                'status':'Ease',
                'author':User.objects.get(username='JamesSong')
            },

            {
                'idx':9,
                'name':lorem.words(4),
                'description':lorem.sentence(),
                'status':'Ease',
                'author':User.objects.get(username='BigBalls')
            },

            {
                'idx':10,
                'name':lorem.words(3),
                'description':lorem.sentence(),
                'status':'Deadline',
                'author':User.objects.get(username='yellow')
            }
        ]

        for note in note_samples:
            noted = Notes.objects.create(
                name=note['name'],
                description=note['description'],
                status=note['status'],
                author=note['author']
            )
            
        
        self.stdout.write(self.style.SUCCESS(f'Created NOTES FINALLY'))




