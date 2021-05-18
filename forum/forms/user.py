from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from forum.models.user import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
