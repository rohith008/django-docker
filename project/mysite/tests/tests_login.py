from django import urls
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import pytest


@pytest.mark.django_db
def test_login_and_logout(client):
    """Tests logging in and logging out"""
    # Create a fake user
    user = User.objects.create_user("my_username")
    user.set_password('my_password123')
    user.save()

    login_url = urls.reverse('login')
    resp = client.post(login_url, {
        'username': 'my_username',
        'password': 'my_password123'
    })

    assert Session.objects.count() == 1