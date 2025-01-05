from django.urls import path
from .views import ProcessDocumentView, StoreAnalysis

urlpatterns = [
    path('process-document/', ProcessDocumentView.as_view(), name='process_document'),
    path('store-analysis/', StoreAnalysis.as_view(), name='store_analysis'),

]
