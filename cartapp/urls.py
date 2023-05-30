from django.urls import path
from cartapp import views
urlpatterns = [
    path('indexpage/', views.indexpage, name='indexpage'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('category/', views.category, name='category'),
]