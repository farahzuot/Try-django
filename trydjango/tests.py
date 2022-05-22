from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfTest(TestCase):
    def test_secret_key_strength(self):
        key = settings.SECRET_KEY
        try:
            is_strong = validate_password(key)
        except Exception as e:
            msg = f'Weak Secret Key {e}'
            self.fail(msg)
