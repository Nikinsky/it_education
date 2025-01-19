
from django.urls import path, include
from .views import *


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', ResetPasswordRequestView.as_view(), name='reset-password'),
    path('reset-password-confirm/<str:token>/', ResetPasswordConfirmView.as_view(), name='reset-password-confirm'),

    path('statya/', StatyaListView.as_view(), name='statya-list'),
    path('statyado/<int:pk>/', StatyDoaDetailView.as_view(), name='statyado-detail'),
    path('statyaposle/<int:pk>/', StatyaPosleDetailView.as_view(), name='statyaposle-detail'),

    path('cours/', CoursListView.as_view(), name='cours-list'),
    path('cours/<int:pk>/', CoursDetailView.as_view(), name='cours-detail'),

    path('masterclass/', MasterClassListView.as_view(), name='masterclass-list'),
    path('masterclass/<int:pk>/', MasterClassDetailView.as_view(), name='masterclass-detail'),

    path('feedback/', FeedBackListView.as_view(), name='feedback-list'),

    path('cart/<int:pk>/', CartViewSet.as_view(), name='cart-detail'),
    path('cart/item/',CartItemViewSet.as_view(), name='cart-item-list'),

    path('visa_cart', VisaCartListView.as_view(), name='visa_cart-list'),

    path('tariff/', TariffView.as_view(), name='tariff-list'),

    path('podpiski/', PodpiskiUserView.as_view(), name='podpiski-list'),

]
