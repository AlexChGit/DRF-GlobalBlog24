from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Create your tests here.


class TestUserUrls(APITestCase):
    user_list_url = reverse('users')

    def setUp(self):
        self.user = self.client.post('/auth/users/', data={'email': 'user3@gmail.com', 'password': 'pass123456789'})
        response = self.client.post('/auth/jwt/create/', data={'email': 'user3@gmail.com', 'password': 'pass123456789'})
        self.token = response.data['access']
        self.user_token_authentication()

    def user_token_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_users_list_when_users_are_authenticated(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_detail_retrieve(self):
        response = self.client.get(reverse('user', kwargs={'pk': 1}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_update(self):
        profile_data = {'username': 'username1', 'lastname': 'lastname1',
                        'about': 'I will use your API', 'password': 'pass123456789'}
        response = self.client.put(reverse('user', kwargs={'pk': 1}), data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
