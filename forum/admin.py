from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from forum.models.user import User
from forum.models.thread import Thread
from forum.models.post import Post
from forum.models.forum import Forum
from forum.forms.user import UserCreationForm, UserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'bio', )
    list_filter = ('email', 'is_staff', 'is_active', 'bio')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'bio')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(User, CustomUserAdmin)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
