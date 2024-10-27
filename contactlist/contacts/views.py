from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from contacts.models import Contact
from django.db.models import QuerySet
from typing import Any

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        
        if q:
            # Filtra los contactos cuyo nombre contiene la consulta (case insensitive)
            return Contact.objects.filter(name__icontains=q)
        
        # Retorna todos los contactos si no hay búsqueda
        return super().get_queryset()

class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth', 'phone')
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth', 'phone')
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
