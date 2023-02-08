from django.contrib import admin
from transactions.models import Deposit, Extraction, Exchange, Transference

# Register your models here.
class DepositAdmin(admin.ModelAdmin):
    pass
class ExtractionAdmin(admin.ModelAdmin):
    pass
class ExchangeAdmin(admin.ModelAdmin):
    pass
class TransferenceAdmin(admin.ModelAdmin):
    pass



admin.site.register(Deposit, DepositAdmin)
admin.site.register(Extraction, ExtractionAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Transference, TransferenceAdmin)
