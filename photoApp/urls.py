from django.urls import path

from . import views


urlpatterns = [
    path('', views.portfolio, name="portfolio" ),
    path('<int:portfolio_id>/', views.detail, name="detail"),
    path('new_photo/', views.new_photo, name='new_photo'),
    path('create_photo/', views.create_photo, name='create_photo'),
]

