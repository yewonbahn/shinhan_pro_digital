from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>",views.ProductDetailView.as_view()),
    path("/<int:pk>/comment",views.CommentDetailView.as_view()),
    path("",views.ProductListView.as_view()),
    path("/comment",views.CommentListView.as_view()),
]