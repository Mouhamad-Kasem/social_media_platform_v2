from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from social.models import User, Post
from social.serializers import UserSerializer, PostSerializer

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)
        self.post_data = {'title': 'Test Post', 'content': 'This is a test post', 'author': self.user}

    def test_create_user(self):
        response = self.client.post(reverse('signup'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_invalid_data(self):
        invalid_data = {'username': 'testuser', 'email': 'invalidemail', 'password': 'short'}
        response = self.client.post(reverse('signup'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_list(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for other user endpoints (PUT, DELETE)

class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        self.user = User.objects.create_user(**self.user_data)
        self.post_data = {'title': 'Test Post', 'content': 'This is a test post', 'author': self.user}

    def test_create_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post_list'), self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_unauthorized(self):
        response = self.client.post(reverse('post_list'), self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_detail(self):
        post = Post.objects.create(**self.post_data)
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


