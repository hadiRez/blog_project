from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='this is a description',
            status=Post.STATUS_CHOICES[0][0],
            author=self.user,
        )

        self.post2 = Post.objects.create(
            title='Post2',
            text='Lorem Ipsum',
            status=Post.STATUS_CHOICES[1][0],
            author=self.user,
        )

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    # def test_post_title_on_blog_list_page(self):
    #     response = self.client.get(reverse('posts_list'))
    #     self.assertContains(response, 'Post1')

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    # def test_post_detail_url_by_name(self):
    #     response = self.client.get(reverse('post_detail', args=[self.post1.id]))
    #     self.assertEqual((response.status_code, 200))

    def test_post_detail_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    # def test_status_code_404_if_post_id_not_exists(self):
    #     response = self.client.get(reverse('post_detail', args=[999])
    #     self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.title)







