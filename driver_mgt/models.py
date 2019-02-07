from django.db import models

from user_mgt.models import UserManagement
from area_db.models import Province, City, Kecamatan, Kelurahan
from payment.models import BankAccount

class Driver(models.Model):
    real_name = models.CharField(max_length=255)
    user = models.OneToOneField(UserManagement, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, db_index=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, db_index=True, null=True)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.SET_NULL, db_index=True, null=True)
    ktp_photo = models.ImageField(upload_to = 'driver/ktp_photo', blank=True)
    is_approved = models.BooleanField(default=False)
    ad_request_approved = models.BooleanField(default=False)
    ad_installation_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
    
    def __str__(self):
        return self.name