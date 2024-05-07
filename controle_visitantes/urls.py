from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views


from apps.dashboard.views import index

from apps.visitantes.views import (
    registrar_visitante,
    informacoes_visitante,
    finalizar_visita,
)

from apps.moradores.views import registrar_morador
from apps.moradores.views import view_morador, info_morador




urlpatterns = [

    path(
        'admin/',
          admin.site.urls,
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'

        ),
        name='login'
    ),
    path(
        'login/',
        auth_views.LogoutView.as_view(
            template_name='logout.html'

        ),
        name='logout'
    ),



    path(
        '',
        index,
        name = 'index',
    ),

    path(
        'registrar/',
        registrar_visitante,
        name = 'registrar_visitante',
    ),

    path(
        'visitantes/<int:id>/',
        informacoes_visitante,
        name = 'informacoes_visitante',
    ),
    path(
        'visitantes/<int:id>/finalizar-visita',
        finalizar_visita,
        name = 'finalizar_visita',
    )

]


urlpatterns += [
    path(
        'registrar-morador/',
        registrar_morador, 
        name='registrar_morador'
    ),

    path(
        'moradores/',
        view_morador,
        name='view_morador'
    ),

    path(
        'morador/<int:id>/',
        info_morador,
        name = 'info_morador'
    ),

   
]