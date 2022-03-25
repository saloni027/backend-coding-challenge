from rest_framework import serializers
from noteapp.models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    """ 
    Serializer for tags 
    """
    
    class Meta:
        model = Tag
        fields = '__all__'
            
class NoteSerializer(serializers.ModelSerializer):
    """ 
    Serializer for Notes 
    """
    note_user = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = '__all__'

   



    

    

    
    