from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# User model: id, firstname[char], latname[char], email[email], username[char], date_of_birth[date], mobile_number[char]
class User(models.Model):
    firstname = models.OneToOneField(User, on_delete=models.CASCADE, null= True, max_length=100)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    mobile_number = models.IntegerField()

    def __str__(self):
        return self.lastname


# project model fields: id, project_name[char-100], text[char-256], translated_to_language[list], created_at[datetime], updated_at[datetime]

languages = [('EN', 'English'),
             ('MA', 'Marathi'),
             ('HI', 'Hindi'),
             ('GJ', 'Gujrati')]


class Project(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length=100)
    text = models.CharField(max_length=256)
    translated_to_language = models.CharField(choices=languages, default='EN', max_length=20)

    def __str__(self):
        return self.project_name


# # order model fields: id, project_id(fk), status[choicefield- new, in-process, complete], translated_text[list], created_at[datetime], updated_at[datetime]

status_choices = [('N', 'New'),
                  ('IP', 'In-Process'),
                  ('C', 'Complete')]


class Order(Base):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices, default='N', max_length=20)
    translated_text = models.CharField(choices=languages, default='EN', max_length=20)

    def __str__(self):
        return self.project_id
