from django.core.management.base import BaseCommand
from Notes.models import Collections , Notes
from django.contrib.auth import get_user_model
import lorem_text 

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a new collection'

    def handle(self,*args,**kwargs):

        collections_arr = [
            {
                'name':'My first collection',
                'description':lorem_text.sentence()
            },

            {
                'name':'My second collection',
                'description':lorem_text.sentence()
            },

            {
                'name':'My third collection',
                'description':lorem_text.sentence()
            },

            {
                'name':'My fourth collection',
                'description':lorem_text.sentence()
            }
        ]