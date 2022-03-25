from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class NoteListTestCase(APITestCase):
    
    def test_note_create(self):
        data = {
            
            "title": "My note",
            "body": "This is my test note",
            "tags": [{"tag_title": "New Tag"}] 
        }
        response = self.client.post(reverse('note-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 
        
class TagListTestCase(APITestCase):
        
    def test_tag_create(self):
        data = {
            
            "tag_title": "My tag"
        }
        response = self.client.post(reverse('tag-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)   
        
                        
    
    
