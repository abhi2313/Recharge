from django.urls import path
from .views import Get_All_recharges, Successful_recharges

urlpatterns = [
    path('get_recharges', Get_All_recharges.as_view()),

    path('successful_recharges', Successful_recharges.as_view())
]
