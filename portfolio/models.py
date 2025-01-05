from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='developer/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

    def __str__(self):
        return self.title

class Language(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='languages/')

    def __str__(self):
        return self.name
