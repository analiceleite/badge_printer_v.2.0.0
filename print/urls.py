from . import utils, views
from django.urls import path

app_name = "print"

urlpatterns = [
    path('', views.render_print, name="render_print" ),
    path('print/', views.print_selected_collaborators, name="print_selected" ),
    path('delete_collaborator/', views.delete_collaborator, name='delete_collaborator'),
    path('edit_collaborator/', views.edit_collaborator, name='edit_collaborator'),
    path('get_collaborator_data/<int:collaborator_id>', utils.get_collaborator_data, name="get_collaborator_data"),
    path('get_collaborator_photo/<int:edv>', utils.get_collaborator_photo, name="get_collaborator_photo"),
]
