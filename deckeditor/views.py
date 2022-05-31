from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Card

class CardListView(ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'list.html'
    paginate_by = 150
    
    def get_queryset(self):
        qs = super().get_queryset()
        searchbox = self.request.GET.get('searchbox')
        format = self.request.GET.get('format')
        if (searchbox):
            filtered = qs.filter(name__icontains=searchbox).filter(legalities__icontains=format)
            return filtered
        else:
            return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('searchbox')
        format = self.request.GET.get('format')
        if (name):
            context['title'] = f'Search Results for {name} in {format}:'
        else:
            context['title'] = 'List of Magic: the Gathering cards'
        self.request.session.set_expiry(0)
        visits = self.request.session.get('visits', 0)
        self.request.session['visits'] = visits+1
        context['visits'] = visits
        return context

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'
    template_name = 'detail.html'