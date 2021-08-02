# Generated by Django 3.2.6 on 2021-08-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Age du client')),
                ('total_relationship_count', models.IntegerField(verbose_name='Nombre total de produits')),
                ('contacts_count_12_mon', models.IntegerField(verbose_name='Nombre de contacts au cours des 12 derniers mois')),
                ('total_revolving_bal', models.IntegerField(verbose_name='Solde renouvelable total sur la carte de crédit')),
                ('avg_open_to_buy', models.FloatField(verbose_name="Ligne de crédit ouverte à l'achat")),
                ('total_amt_chng_q4_q1', models.FloatField(verbose_name='Changement du montant de la transaction')),
                ('total_trans_amt', models.FloatField(verbose_name='Montant total de la transaction')),
                ('total_trans_ct', models.FloatField(verbose_name='Nombre total de transactions')),
                ('total_ct_chng_q4_q1', models.FloatField(verbose_name='Changement du nombre de transactions')),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]
