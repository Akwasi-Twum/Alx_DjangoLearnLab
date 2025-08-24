from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post
from notifications.models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='pass')
        self.user2 = get_user_model().objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(owner=self.user1, content='Test')

    def test_like_notification(self):
        self.client.login(username='user2', password='pass')
        self.client.post(f'/posts/{self.post.id}/like/')
        self.assertTrue(Notification.objects.filter(recipient=self.user1, actor=self.user2, verb='liked your post').exists())