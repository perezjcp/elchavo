from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from . models import Sales, SalesForm
from django.db.models import Sum


# Create your views here.
@login_required()
def index(request):
    return render(request, "getsales/index.html")

@login_required()
def getinfo(request):
    return render(request, "getsales/getinfo.html")

@login_required()
def msales(request):
    """Return sales function."""
    month = int(request.POST["month"])
    year = int(request.POST["year"])
    date = (request.POST["date"])
    if date:
        ldate = datetime.strptime(date, "%Y-%m-%d")
        sales = Sales.objects.filter(date__month = ldate.month, date__year = ldate.year, date__day = ldate.day)
    if month > 0:
        lyear = datetime.now().year
        sales = Sales.objects.filter(date__month = month, date__year = lyear)
    if year > 0:
        sales = Sales.objects.filter(date__year = year)
    context = {
       "sales": sales,
       "tcash_sales": sales.aggregate(Sum("cash_sales")),
        "tcredit_sales": sales.aggregate(Sum("credit_sales")),
        "ttips": sales.aggregate(Sum("tips")),
        "tsavings": sales.aggregate(Sum("savings")),
        "tcash_pay": sales.aggregate(Sum("cash_pay")),
        "tcash_exp": sales.aggregate(Sum("cash_exp")),
    }
    return render(request, "getsales/msales.html", context)  

@login_required()
def update(request):
    """Update the sales for a date"""
    sales = SalesForm(request.POST)
    if sales.is_valid():
        sales_tran = sales.save(commit=False)
        sales_tran.owner = request.user
        sales_tran.save()
        #owner = request.user
        #date = request.POST["date"]
        #cash_sales = request.POST["cash_sales"]
        #credit_sales = request.POST["credit_sales"]
        #savings = request.POST["savings"]
        #tips = request.POST["tips"]
        #cash_exp = request.POST["cash_exp"]
        #cash_pay = request.POST["cash_pay"]
        #notes = request.POST["notes"]
        #sales = Sales(owner = owner, savings = savings, date = date, cash_sales = cash_sales, credit_sales = credit_sales, tips = tips, cash_exp = cash_exp, cash_pay = cash_pay, notes= notes)
        #sales.save()
        context = {
        "sales" : sales_tran,
        }
        return render(request, "getsales/response.html", context)

    else:
        context = {
            "sales" : sales,
            "error" : "Error. Solo numeros enteros y decimals"
            }
        return render(request, "getsales/inputsales.html", context)



@login_required()
def inputsales(request):
    form = SalesForm(request.POST)
    context = {'form' : form}
    return render(request, "getsales/inputsales.html", context)  

def log_out(request):
    logout(request)
    return render(request, "registration/logout.html")


