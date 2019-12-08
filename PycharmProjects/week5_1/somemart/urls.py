from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/goods/', views.AddItemView.as_view()),
    path('api/v1/goods/<int:item_id>/reviews/', views.PostReviewView.as_view()),
    path('api/v1/goods/<int:item_id>/', views.GetItemView.as_view()),
]
