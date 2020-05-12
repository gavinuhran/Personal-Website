from django.contrib import admin
from .models import ProfilePicture
from .models import LinkedIn, Twitter, Instagram, GitHub
from .models import FeaturedProject
from .models import Project

admin.site.register(ProfilePicture)
admin.site.register(LinkedIn)
admin.site.register(Twitter)
admin.site.register(Instagram)
admin.site.register(GitHub)
admin.site.register(FeaturedProject)
admin.site.register(Project)