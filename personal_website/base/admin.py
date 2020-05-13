from django.contrib import admin
from .models import Profile
from .models import AboutMe
from .models import LinkedIn, Twitter, Instagram, GitHub
from .models import FeaturedProject
from .models import Project

admin.site.register(Profile)
admin.site.register(AboutMe)
admin.site.register(LinkedIn)
admin.site.register(Twitter)
admin.site.register(Instagram)
admin.site.register(GitHub)
admin.site.register(FeaturedProject)
admin.site.register(Project)