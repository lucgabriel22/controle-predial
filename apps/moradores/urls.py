from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


from apps.moradores.views import (
    MoradorCreateView,
    MoradorListView,
    MoradorUpdateView,
    MoradorDeleteView,
    MoradorDetailView,
    MoradorDatatableView,
    
)



app_name = 'moradores'




urlpatterns = [
    path(
        'registrar/',
        views.MoradorCreateView.as_view(), 
        name='registrar'
    ),

    path(
        'listar/',
        views.MoradorListView.as_view(),
        name='listar'
    ),

    path(
        'datatable/',
        views.MoradorDatatableView.as_view(),
        name='datatable'
    ),

    path(
        '<int:pk>',
        views.MoradorDetailView.as_view(),
        name = 'detalhe'
    ),

    path(
        '<int:pk>/atualizar',
        views.MoradorUpdateView.as_view(),
        name='atualizar'
    ),

    path(
        '<int:pk>/deletar',
        views.MoradorDeleteView.as_view(),
        name='deletar'
    )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)