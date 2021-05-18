from django.views.generic.list import ListView
from forum.models.forum import Forum


class Homepage(ListView):
  model = Forum
  # template_name = 'homepage_list.html'
