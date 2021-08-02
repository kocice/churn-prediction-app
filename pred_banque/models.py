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

