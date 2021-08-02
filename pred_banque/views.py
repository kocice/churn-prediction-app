from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import joblib
from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):
    # if request.POST.get('action') == 'post':
    if request.method == 'POST':
        # Receive data from client
        age = int(request.POST.get('age'))
        total_relationship_count = int(request.POST.get('total_relationship_count'))
        contacts_count_12_mon = int(request.POST.get('contacts_count_12_mon'))
        total_revolving_bal = int(request.POST.get('total_revolving_bal'))
        avg_open_to_buy = float(request.POST.get('avg_open_to_buy'))
        total_amt_chng_q4_q1 = float(request.POST.get('total_amt_chng_q4_q1'))
        total_trans_amt = int(request.POST.get('total_trans_amt'))
        total_trans_ct = int(request.POST.get('total_trans_ct'))
        total_ct_chng_q4_q1 = float(request.POST.get('total_ct_chng_q4_q1'))

        info = [
            age, total_relationship_count, contacts_count_12_mon, total_revolving_bal,
            avg_open_to_buy, total_amt_chng_q4_q1, total_trans_amt, total_trans_ct, total_ct_chng_q4_q1
        ]

        variable = ['Customer_Age', 'Total_Relationship_Count', 'Contacts_Count_12_mon',
                    'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1',
                    'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1']

        # Unpickle model
        norm = joblib.load(r'ma_normalisation.pkl')
        model = joblib.load(r"mon_modele_banque.pkl")

        # Make prediction
        data = pd.DataFrame(info, index=variable).T
        data[variable] = norm.transform(data)
        result = model.predict(data)
        pourcent = model.predict_proba(data)

        # On recupère la prediction
        pred = result[0]
        if pred == 0:
            classification = 'Existing Customer'
        else:
            classification = 'Attrited Customer'

        pred = PredResults(age=age, total_relationship_count=total_relationship_count,
                           contacts_count_12_mon=contacts_count_12_mon, total_revolving_bal=total_revolving_bal,
                           avg_open_to_buy=avg_open_to_buy, total_amt_chng_q4_q1=total_amt_chng_q4_q1,
                           total_trans_amt=total_trans_amt, total_trans_ct=total_trans_ct,
                           total_ct_chng_q4_q1=total_ct_chng_q4_q1, classification=classification
                           )
        pred.save()

        return JsonResponse({'result': classification, 'age': age, 'total_relationship_count': total_relationship_count,
                             'contacts_count_12_mon': contacts_count_12_mon, 'total_revolving_bal': total_revolving_bal,
                             'avg_open_to_buy': avg_open_to_buy, 'total_amt_chng_q4_q1': total_amt_chng_q4_q1,
                             'total_trans_amt': total_trans_amt, 'total_trans_ct': total_trans_ct,
                             'total_ct_chng_q4_q1': total_ct_chng_q4_q1},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
