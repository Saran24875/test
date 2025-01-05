from django.shortcuts import render
from .models import Developer, Skill, Project, Language

def index(request):
    developer = Developer.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    languages = Language.objects.all()
    return render(request, 'portfolio/index.html', {
        'developer': developer,
        'skills': skills,
        'projects': projects,
        'languages': languages,
    })

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})
