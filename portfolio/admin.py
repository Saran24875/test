from django.contrib import admin
from .models import Developer, Skill, Project, Language

admin.site.register(Developer)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Language)
