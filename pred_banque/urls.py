from django.urls import path
from . import views

app_name = "pred_banque"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('predict_db/', views.view_predict_db, name='predict_db'),
]
