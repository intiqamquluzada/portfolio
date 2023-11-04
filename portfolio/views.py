from django.shortcuts import render
from portfolio.models import (SocialMedia, About, Awards, Experience, Projects,
                              Education, Interest, Skills, )


def home_view(request):
    socials = SocialMedia.objects.all()
    about = About.objects.last()
    awards = Awards.objects.order_by("-created_at")
    experiences = Experience.objects.order_by("-created_at")
    educations = Education.objects.order_by("-created_at")
    interest = Interest.objects.last()
    skills = Skills.objects.order_by("-created_at")
    projects = Projects.objects.order_by("-created_at")
    context = {
        "socials": socials,
        "about": about,
        "awards": awards,
        'experiences': experiences,
        'educations': educations,
        'interest': interest,
        'skills': skills,
        'projects': projects,
    }
    return render(request, "index.html", context)


