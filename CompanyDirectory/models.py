from django.db import models

# class Company(models.Model):
#     name = models.CharField(max_length=20, null=False, blank=False, primary_key=True)
#     description = models.CharField(max_length=100,null=True)
#     address = models.ForeignKey('Address', null=True, blank=True, on_delete=models.SET_NULL)
#     phone = models.CharField(max_length=20, null=True)
#
#     def __str__ (self):
#         return self.name



class Address(models.Model):
    # id = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    companyName = models.CharField(max_length=20, primary_key=True)
    buildingNumber = models.IntegerField(null=True, blank=True)
    postalCode = models.IntegerField(null=True, db_index=True)
    locality = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True, db_index=True)
    state = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.companyName)