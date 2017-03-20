from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def index(request):
    r = requests.get("http://193.142.112.220:8337/companyList")
    company_data = r.json()
    return render(request, 'recrut/index.html', {"data": company_data})


@login_required
def materialy(request):
    r = requests.get("http://193.142.112.220:8337/materialList")
    materialy_data = r.json()
    return render(request, 'recrut/materialy.html', {"data": materialy_data})


@login_required
def more(request, company_id):
    """
    THis view is responsible for doing nothing.

    :param request: view request
    :param int company_id: ID of the company bla bla
    :retrun: rendered view
    """
    r = requests.get(
        "http://193.142.112.220:8337/materialList",
        params={"companyID": company_id}
    )
    more_data = r.json()
    return render(request, 'recrut/materialy.html', {"data": more_data})
