from django.test import TestCase
from .models import *
from django.apps import apps


class PostModelTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.create_superuser(
            username='admin', 
            email='admin@gmail.com', 
            password='admin')
        self.post = Post.objects.create(
            title='Title',
            content='Post content',
            author=user,
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_auto_populate_updated_on(self):
        self.assertIsNotNone(self.post.updated_on)

        old_post_updated_on = self.post.updated_on
        self.post.content = 'New post content'
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.updated_on > old_post_updated_on)

    

