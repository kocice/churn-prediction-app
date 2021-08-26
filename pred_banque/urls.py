from django.urls import path
from . import views

app_name = "pred_banque"

urlpatterns = [
    # path('', views.predict, name='prediction_page'),
    path('', views.view_dash, name='dash'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('predict_db/<int:nb_page>/', views.view_predict_db, name='predict_db'),
    path('results_db/', views.view_predict_db, name='results_db'),
    path('upload_data/', views.upload_data, name='upload_data'),
    path('affiche_data/', views.affiche_data, name='affiche_data')
]
