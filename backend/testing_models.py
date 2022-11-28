import forms
import models

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    user = models.User.signup(
        username='Phil',
        email='test@test.com', 
        password='password123'
        )

    assert user.email == 'test@test.com'
    assert user.username == 'Phil'
    assert user.password != 'password123'

test_new_user()