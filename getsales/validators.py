from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_decimal(value):
    print("inside validate")
    if not int(value) and not float(value):
        raise ValidationError(_("Solo numeros decimales"))
    return value