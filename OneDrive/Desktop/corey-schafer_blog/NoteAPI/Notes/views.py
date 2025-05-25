from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def all_notes(request):
    notes = Notes.objects.all()
    serialized_notes = NotesSerializer(notes,many=True)
    return Response(serialized_notes.data)

@api_view(['GET'])
def note_id(request,pk):
    note = get_object_or_404(Notes,pk=pk)
    serialized_note = NotesSerializer(note)
    return Response(serialized_note.data)
