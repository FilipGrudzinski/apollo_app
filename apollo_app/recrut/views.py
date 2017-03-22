from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def index(request):
    """
    This view is responsible for show company list.
    :param request: view request
    :retrun: rendered view
    """
    r = requests.get("http://193.142.112.220:8337/companyList")
    company_data = r.json()
    return render(request, 'recrut/index.html', {"data": company_data})


@login_required
def material(request):
    """
    This view is responsible for show materials.
    :param request: view request
    :retrun: rendered view
    """
    r = requests.get("http://193.142.112.220:8337/materialList")
    material_data = r.json()
    return render(request, 'recrut/material.html', {"data": material_data})


@login_required
def details(request, company_id):
    """
    This view is responsible for show material list assigned to company.
    :param request: view request
    :param int company_id: ID of the company
    :retrun: rendered view
    """
    r = requests.get(
        "http://193.142.112.220:8337/materialList",
        params={"companyID": company_id}
    )
    details_data = r.json()
    return render(request, 'recrut/material.html', {"data": details_data})
