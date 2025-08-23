from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostCommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(author=self.user, title='Test', content='Test content')
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Nice post!')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test')

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Nice post!')