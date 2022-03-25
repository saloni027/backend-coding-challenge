from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from noteapp.models import Note, Tag
from noteapp.serializers import NoteSerializer, TagSerializer

 #TODO Seprate List and CreateView and and remove permission for public notes
class NoteList(generics.ListCreateAPIView):
    """ 
    Class Based View for Listing and Creating Notes 
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    
    def perform_create(self, serializer):
        """ 
        Override perform_create method to add tags with a POST request 
        """
        data = self.request.data
        note_user = self.request.user
        new_note = Note.objects.create(title=data["title"],body=data["body"], note_user=note_user)
        new_note.save()
        
        for tag in data["tags"]:
            tag_obj, bool_result = Tag.objects.get_or_create(tag_title=tag["tag_title"])
            new_note.tags.add(tag_obj)
            
        serializer = NoteSerializer(new_note)
        return Response(serializer.data)
    
    def get_queryset(self):
        """ 
        Override get_queryset method for filtering queryset with tags and keywords 
        """
        queryset = Note.objects.filter(note_user=self.request.user)
        tag = self.request.query_params.get('tag', None)
        keyword = self.request.query_params.get('keyword', None) 
        
        if tag:     #TODO Add functionality for filtering notes by multiple tags
            queryset = Note.objects.filter(tags__tag_title=tag, note_user=self.request.user)
        if keyword:
            queryset = Note.objects.filter(body__contains=keyword, note_user=self.request.user)
        return queryset
    
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Class Based Detail View for Retriving, Updating and Deleting Notes 
    """ 
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def update(self, request, *args, **kwargs):
        """ 
        Override update method to update tags with a PUT request 
        """
        data = self.request.data
        note_obj = self.get_object()
        current_attached_tags = note_obj.tags.all()
        for tag in current_attached_tags: #removing olders set of tags
            note_obj.tags.remove(tag)
            
        for tag in data["tags"]: #attaching new set of tags
            tag_obj, bool_result = Tag.objects.get_or_create(tag_title=tag["tag_title"])
            note_obj.tags.add(tag_obj)
            
        note_obj.title = data['title']
        note_obj.body = data['body']
            
        serializer = NoteSerializer(note_obj)
        return Response(serializer.data)
    
class TagList(generics.ListCreateAPIView):
    """ 
    Class Based View for Listing and Creating Tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Class Based Detail View for Retriving, Updating and Deleting Tags 
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    



            