from django.shortcuts import render
from .models import Profile
from .models import AboutMe
from .models import LinkedIn, Twitter, Instagram, GitHub
from .models import FeaturedProject
from .models import Project

# Create your views here.
def home(request):
    profiles = Profile.objects.all()
    aboutMes = AboutMe.objects.all()
    linkedinLinks = LinkedIn.objects.all()
    twitterLinks = Twitter.objects.all()
    instagramLinks = Instagram.objects.all()
    githubLinks = GitHub.objects.all()
    featuredProjects = FeaturedProject.objects.all().order_by('-date')
    return render(request, 'base/home.html', {'profiles': profiles, 'aboutMes': aboutMes, 'linkedinLinks': linkedinLinks, 'twitterLinks': twitterLinks, 'instagramLinks': instagramLinks, 'githubLinks': githubLinks, 'featuredProjects': featuredProjects})

def projects(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'base/projects.html', {'projects': projects})