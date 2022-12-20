from django.contrib import admin

# Register your models here.

from.models import Recharge, SuccessfulRecharge


admin.site.register(Recharge)
admin.site.register(SuccessfulRecharge)
