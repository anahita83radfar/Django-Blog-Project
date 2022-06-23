from django.test import TestCase
from .forms import CommentForm, PostForm


class TestCommentForm(TestCase):
    
    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
        
    def test_comment_form_is_valid(self):
        form = CommentForm({'body': 'Test comment'})
        self.assertTrue(form.is_valid())
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
        

class TestPostForm(TestCase):
    
    def test_post_title_is_required(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        
    def test_post_content_is_required(self):
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
        
    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'content'])
        
    def test_post_form_is_valid(self):
        form = PostForm({'title': 'Post', 'content': 'Post content'})
        self.assertTrue(form.is_valid())
    
