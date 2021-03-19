from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView
app_name = 'realtors'
urlpatterns = [
    path('', RealtorListView.as_view(), name='realtors'),
    path('topseller', TopSellerView.as_view(), name='topseller'),
    path('<pk>', RealtorView.as_view(), name='realtor'),
]
