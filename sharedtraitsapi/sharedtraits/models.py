from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValidationError("User must provide an email.")
        if not username:
            raise ValidationError("User must provide a username.")
        if not password:
            raise ValidationError("User must provide a password.")

        user = self.model(
            email = self.normalize_email(email)
        )

        user.username = username
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValidationError("User must provide an email.")
        if not username:
            raise ValidationError("User must provide a username.")
        if not password:
            raise ValidationError("User must provide a password.")
        
        user = self.model(
            email = self.normalize_email(email)
        )

        user.username = username
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, username, password=None):
        if not email:
            raise ValueError("User must provide an email.")
        if not username:
            raise ValueError("User must provide a username.")
        if not password:
            raise ValueError("User must provide a password.")

        user = self.model(
            email = self.normalize_email(email)
        )

        user.username = username
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, ('Admin User')),
        (STAFF, ('Staff User')),
    ]

    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(('username'), max_length=20)
    tags = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        #Does the user have a specific permission?
        #Simplest answer: Yes, always
        return True
    
    @staticmethod
    def has_module_perms(app_label):
        #Does the user have permissions to view the app 'app_label'?
        #Simplest answer: Yes, alway
        return True

    def __str__(self):
        return "{}".format(self.email)

class UserAnswerModel(models.Model):
    userID = models.IntegerField(default=-1)
    questionID = models.IntegerField(default=-1)
    answerID = models.IntegerField(default=-1)

class QuestionModel(models.Model):
    question = models.TextField(default="")
    answers = models.JSONField(default=dict)
    tags = models.JSONField(default=dict)