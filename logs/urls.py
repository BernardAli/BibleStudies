from django.urls import path
from .views import index_page, topics, topic, new_topic, new_entry, edit_entry

app_name = 'logs'

urlpatterns = [
    path("", index_page, name="home"),
    path("topics/", topics, name="topics"),
    path('topic/<str:title_id>/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:title_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
]