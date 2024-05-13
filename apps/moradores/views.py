from apps.moradores.forms import MoradorForm
from moradores.models import Moradores
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy






class MoradorDetailView(LoginRequiredMixin, DetailView):
    model = Moradores
    template_name = 'info_morador.html'
    context_object_name = 'morador'  # Renomeie para 'morador' para representar um único objeto
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class MoradorCreateView(LoginRequiredMixin, CreateView):
    model = Moradores
    # Formulário que será usado para criar a instância.
    form_class = MoradorForm
    template_name = 'registrar_morador.html'
    success_url = reverse_lazy('index')


class MoradorUpdateView(LoginRequiredMixin, UpdateView):
    model = Moradores
    form_class = MoradorForm
    template_name = 'atualizar_morador.html'
    context_object_name = 'moradores'
    success_url = reverse_lazy('index')
    

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class MoradorListView(LoginRequiredMixin, ListView):
    model = Moradores
    template_name = 'view_morador.html'
    context_object_name = 'moradores'
    paginate_by = 5

    def get_queryset(self):
        # Ordene the QuerySet pelo a campo específico, for example, 'criado'
        return Moradores.objects.all().order_by('-numero_casa')


class MoradorDatatableView(LoginRequiredMixin, ListView):
    model = Moradores
    template_name = 'view_morador.html'
    context_object_name = 'moradores'
    paginate_by = 5

    def get_queryset(self):
        # Ordene the QuerySet pelo a campo específico, for example, 'criado'
        return Moradores.objects.all().order_by('-numero_casa')


class MoradorDeleteView(LoginRequiredMixin, DeleteView):
    model = Moradores
    template_name = 'deletar_morador.html'
    success_url = reverse_lazy('index')









    





   









