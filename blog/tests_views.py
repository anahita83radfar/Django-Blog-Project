from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class testView(TestCase):

    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_post_detail(self):
        user = User.objects.create(username='user', password='password')
        post = Post.objects.create(title='Post', author=user)
        response = self.client.get(f'/{post.slug}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_login(self):
        response = self.client.get('/new/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_post_create(self):
        user = User.objects.create_user(username='user', password='password')
        self.login_url = reverse('post_create')

    def test_post_update_login(self):
        user = User.objects.create(username='user', password='password')
        post = Post.objects.create(title='Post', author=user)
        response = self.client.get(f'/{post.slug}/update/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_post_update(self):
        user = User.objects.create_user(username='user', password='password')
        self.login_url = reverse('post_update', kwargs={'slug': 'slug'})

    def test_post_detail_delete_login(self):
        user = User.objects.create(username='user', password='password')
        post = Post.objects.create(title='Post', author=user)
        response = self.client.get(f'/{post.slug}/delete/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_post_detail_delete(self):
        user = User.objects.create_user(username='user', password='password')
        self.login_url = reverse('post_detail', kwargs={'slug': 'slug'})

    def test_profile_login(self):
        user = User.objects.create(username='user', password='password')
        post = Post.objects.create(title='Post', author=user)
        response = self.client.get('/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_profile(self):
        user = User.objects.create_user(username='user', password='password')
        self.login_url = reverse('profile')

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
