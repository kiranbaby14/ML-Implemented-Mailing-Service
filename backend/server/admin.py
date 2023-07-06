from django.contrib import admin
from .models import UserAccount, Tag, UserTagPreference, TagLabels


# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(TagLabels)
class TagLabelsAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTagPreference)
class UserTagPreferenceAdmin(admin.ModelAdmin):
    exclude = ('tag',)
