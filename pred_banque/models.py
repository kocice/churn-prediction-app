from django.db import models


class PredResults(models.Model):
    age = models.IntegerField(verbose_name='Age du client', )
    total_relationship_count = models.IntegerField(verbose_name='Nombre total de produits', )
    contacts_count_12_mon = models.IntegerField(verbose_name='Nombre de contacts au cours des 12 derniers mois', )
    total_revolving_bal = models.IntegerField(verbose_name='Solde renouvelable total sur la carte de crédit', )
    avg_open_to_buy = models.FloatField(verbose_name="Ligne de crédit ouverte à l'achat")
    total_amt_chng_q4_q1 = models.FloatField(verbose_name="Changement du montant de la transaction")
    total_trans_amt = models.FloatField(verbose_name="Montant total de la transaction")
    total_trans_ct = models.FloatField(verbose_name="Nombre total de transactions")
    total_ct_chng_q4_q1 = models.FloatField(verbose_name="Changement du nombre de transactions")
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification


class BankData(models.Model):
    attrition_flag = models.CharField(db_column='Attrition_Flag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_age = models.IntegerField(db_column='Customer_Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dependent_count = models.IntegerField(db_column='Dependent_count', blank=True, null=True)  # Field name made lowercase.
    education_level = models.CharField(db_column='Education_Level', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    income_category = models.CharField(db_column='Income_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_category = models.CharField(db_column='Card_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    months_on_book = models.IntegerField(db_column='Months_on_book', blank=True, null=True)  # Field name made lowercase.
    total_relationship_count = models.IntegerField(db_column='Total_Relationship_Count', blank=True, null=True)  # Field name made lowercase.
    months_inactive_12_mon = models.IntegerField(db_column='Months_Inactive_12_mon', blank=True, null=True)  # Field name made lowercase.
    contacts_count_12_mon = models.IntegerField(db_column='Contacts_Count_12_mon', blank=True, null=True)  # Field name made lowercase.
    credit_limit = models.FloatField(db_column='Credit_Limit', blank=True, null=True)  # Field name made lowercase.
    total_revolving_bal = models.IntegerField(db_column='Total_Revolving_Bal', blank=True, null=True)  # Field name made lowercase.
    avg_open_to_buy = models.FloatField(db_column='Avg_Open_To_Buy', blank=True, null=True)  # Field name made lowercase.
    total_amt_chng_q4_q1 = models.FloatField(db_column='Total_Amt_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    total_trans_amt = models.IntegerField(db_column='Total_Trans_Amt', blank=True, null=True)  # Field name made lowercase.
    total_trans_ct = models.IntegerField(db_column='Total_Trans_Ct', blank=True, null=True)  # Field name made lowercase.
    total_ct_chng_q4_q1 = models.FloatField(db_column='Total_Ct_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    avg_utilization_ratio = models.FloatField(db_column='Avg_Utilization_Ratio', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    predict = models.CharField(db_column='Predict', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.attrition_flag

    class Meta:
        managed = False
        db_table = 'bank_data'

