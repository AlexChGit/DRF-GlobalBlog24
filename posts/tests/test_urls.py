from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Create your tests here.


class TestPostUrls(APITestCase):
    posts_list_url = reverse('posts')

    def setUp(self):
        self.post = self.client.post('/api/v1/post/create/', data={'title': 'new post', 'body': 'new post body here'})

    def test_posts_list(self):
        response = self.client.get(self.posts_list_url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCommentUrls(APITestCase):
    comments_list_url = reverse('comments')

    def setUp(self):
        self.post = self.client.post('/api/v1/post/create/', data={'title': 'new post', 'body': 'new post body here'})
        self.post = self.client.post('/api/v1/comment/create/', data={'post': '1', 'name': 'new comment',
                                                                      'body': 'new comment body here'})

    def test_comments_list(self):
        response = self.client.get(self.comments_list_url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
