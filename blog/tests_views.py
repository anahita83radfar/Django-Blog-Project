from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class testView(TestCase):
    
    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_get_post_detail(self):
        user=User.objects.create(username='user', password='password')
        post=Post.objects.create(title='Post', author=user)
        response = self.client.get(f'/{post.slug}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
    
    # def test_post_create(self):
    #     response = self.client.get('/new/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_form.html')