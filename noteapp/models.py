from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    """ 
    Tags to categorize notes
    """
    tag_title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        """ Return a string representation of the model. """
        return self.tag_title
    
class Note(models.Model):
    """ 
    A Note user wants to make
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)
    note_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    # public = models.BooleanField(default=False)  
        
    def __str__(self) -> str:
        """ Return a string representation of the model. """
        return self.title


