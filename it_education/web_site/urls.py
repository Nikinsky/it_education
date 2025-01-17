from django.urls import path, include
from .views import *


urlpatterns = [
    path('statya/', StatyaListView.as_view(), name='statya-list'),
    path('statya/<int:pk>/', StatyaDetailView.as_view(), name='statya-detail'),
    path('cours/', CoursListView.as_view(), name='cours-list'),
    path('cours/<int:pk>/', CoursDetailView.as_view(), name='cours-detail'),
    path('masterclass/', MasterClassListView.as_view(), name='masterclass-list'),
    path('masterclass/<int:pk>/', MasterClassDetailView.as_view(), name='masterclass-detail'),
    path('feedback/', FeedBackListView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedBackDetailView.as_view(), name='feedback-detail'),
]
