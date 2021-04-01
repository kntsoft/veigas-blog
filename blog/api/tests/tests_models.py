from django.test import TestCase
from api.models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(
            username='testuser1', password='12345')
        Post.objects.create(title='Title', body='Text Body', owner=user1)

    def test_title_label(self):
        post = Post.objects.get(id=1)
        title = post._meta.get_field('title').verbose_name
        self.assertEquals(title, 'title')

    def test_body_label(self):
        post = Post.objects.get(id=1)
        body = post._meta.get_field('body').verbose_name
        self.assertEquals(body, 'body')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
