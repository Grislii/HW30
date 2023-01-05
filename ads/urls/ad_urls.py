from django.urls import path

from ads.views import AdDetailView, AdsUploadView, AdListView, AdsCreateView, AdDeleteView, AdUpdateView

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('create/', AdsCreateView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdsUploadView.as_view()),
]
