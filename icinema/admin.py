from django.contrib import admin
import models
# Register your models here.
admin.site.register(models.Cinema)
admin.site.register(models.Performances)
admin.site.register(models.Films)
admin.site.register(models.CinemaReview)