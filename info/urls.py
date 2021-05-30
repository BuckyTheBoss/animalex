from django.urls import path
from . import views


urlpatterns = [
    path('animals/', views.AnimalListView.as_view(), name='all_animals'),
    path('specific/animals/', views.FourLeggedAnimalListView.as_view(), name='specific_animals'),
    path('animal/<int:pk>/', views.AnimalDetailView.as_view(), name='single_animal'),
    path('family/<int:family_id>/', views.single_family, name='single_family'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('add_animal_model/', views.AnimalCreateView.as_view(), name='add_animal_model'),
    path('add_family/', views.add_family, name='add_family'),
    path('add_person/', views.add_person, name='add_person'),
    path('add_passport/', views.add_passport, name='add_passport'),
    path('view_person/<int:person_id>/', views.person_details, name='person_deets'),
    path('', views.HomepageView.as_view(), name='homepage')
]

