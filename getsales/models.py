from django.db import models
from django.forms import ModelForm
from django.conf import settings
from .validators import validate_decimal

User = settings.AUTH_USER_MODEL
# Create your models here.
class Sales(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    date        = models.DateField(auto_now=False)
    cash_sales  = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=2, validators=[validate_decimal])
    credit_sales = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=2, validators=[validate_decimal])
    savings     = models.DecimalField(max_digits=7, null=True,  blank=True, decimal_places=2, validators=[validate_decimal])
    tips        = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=2, validators=[validate_decimal])
    cash_exp    = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=2, validators=[validate_decimal])
    cash_pay    = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=2, validators=[validate_decimal])
    notes       = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return f"Fecha:{self.date} - Efectivo:{self.cash_sales} -Savings: {self.savings} - Credito:{self.credit_sales} - Tips:{self.tips} - Gastos Efectivo:{self.cash_exp} - Pagos Efectivo:{self.cash_pay}"
    
class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['date', 'cash_sales', 'credit_sales', 'savings', 'tips', 'cash_exp', 'cash_pay', 'notes']
