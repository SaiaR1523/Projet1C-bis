from django.db import models


class Dtlfact(models.Model):
    iddtfact = models.AutoField(db_column='idDtFact', primary_key=True)  # Field name made lowercase.
    qte = models.IntegerField(blank=True, null=True)
    numfacture = models.ForeignKey('Facture', models.DO_NOTHING, db_column='numFacture', blank=True, null=True)  # Field name made lowercase.
    numproduit = models.ForeignKey('Produit', models.DO_NOTHING, db_column='numProduit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DTLFACT'


class Facture(models.Model):
    numfacture = models.TextField(db_column='numFacture', primary_key=True)  # Field name made lowercase.
    pays = models.ForeignKey('Pays', models.DO_NOTHING, db_column='pays', blank=True, null=True)
    datefact = models.DateField(db_column='dateFact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTURE'


class Pays(models.Model):
    pays = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'PAYS'


class Produit(models.Model):
    numproduit = models.TextField(db_column='numProduit', primary_key=True)  # Field name made lowercase.
    nomproduit = models.TextField(db_column='nomProduit', blank=True, null=True)  # Field name made lowercase.
    pu = models.TextField(db_column='PU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUIT'