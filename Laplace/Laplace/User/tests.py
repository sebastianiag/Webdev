from rest_framework.test import APIClient, APITestCase
from rest_framework import status



class SomeTest(APITestCase):

    def test_create_user(self):

        client = APIClient(enforce_csrf_checks=True)
        response = client.post('http://127.0.0.1:8000/api/v1/users', {'email': 'sawari@gmail.com', 'username': 'sawari', 'password':'123456'}, format='json')
        get_response = client.get('/api/v1/users')
        print get_response.content
        
        client.login(email='sawari@gmail.com', password='123456')
        client.logout()

