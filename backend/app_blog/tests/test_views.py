from django.test import TestCase, override_settings
from app_blog.models import Post
from app_account.models import User
from django.urls import reverse


class BlogPagetest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="user1", password="userpass", email="user@user.com"
        )
        self.post1 = Post.objects.create(title="t1", body="b1", author=user)
        self.post2 = Post.objects.create(title="t2", body="b2", author=user)

    def test_blog_page_returns_correct_response_with_context(self):
        response = self.client.get(reverse("app_blog:blog"))
        self.assertTemplateUsed(response, "app_blog/blog.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "t1")

    def test_blog_page_returns_correct_response_without_context(self):
        # self.post1.delete()
        # self.post2.delete()
        Post.objects.all().delete()
        response = self.client.get(reverse("app_blog:blog"))

        self.assertContains(response, "No post available right now")


class SinglePostpagetest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="user1", password="userpass", email="user@user.com"
        )
        self.post1 = Post.objects.create(title="t1", body="b1", author=user)
        self.post2 = Post.objects.create(title="t2", body="b2", author=user)

    def test_single_post_page_returns_correct_response_with_context(self):

        # below two responses have a same result
        # response = self.client.get(
        #     reverse("app_blog:single_post", kwargs={"id": self.post1.id})
        # )
        response = self.client.get(self.post1.get_absolute_url())
        self.assertTemplateUsed(response, "app_blog/single_post.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "t1")

    @override_settings(DEBUG=False)
    def test_single_post_page_id_does_not_exists(self):

        Post.objects.all().delete()
        response = self.client.get(reverse("app_blog:single_post", kwargs={"id": 5}))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
        print(f"404 page contains ========================== {response.content}")
        # self.assertContains(response, "PAGE NOTTTTTTTT FOUND")
