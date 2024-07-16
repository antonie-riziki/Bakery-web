from django.contrib import admin
from .models import *

admin.site.site_header = 'NC Admin'

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(GraduationCake)
admin.site.register(ThemedCake)
admin.site.register(BirthdayCake)
admin.site.register(BabyShowerCake)
admin.site.register(WeddingCake)
admin.site.register(CupCake)

