from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email='', name='', password=None):
        """Create and return a `User` with an email and password."""
        if not email:
            raise TypeError('Users must have an email address')

        user = self.model(name=name, email=self.normalize_email(email))
        print(password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name='', password=None):
        """
        Create and return a `User` with superuser permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.save()

        return user
