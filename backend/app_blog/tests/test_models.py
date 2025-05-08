from django.test import TestCase
from app_blog.models import Post
from app_account.models import User


class PostModelTest(TestCase):

    def test_model_without_object(self):
        posts = Post.objects.all()

        self.assertEqual(str(posts), "<QuerySet []>")

    def test_string_method(self):
        user = User.objects.create_user(
            username="user1", password="userpass", email="user@user.com"
        )
        post = Post.objects.create(title="t1", body="b1", author=user)

        self.assertEqual(str(post), post.title)
