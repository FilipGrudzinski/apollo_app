from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def company(request):
    """
    This view is responsible for show company list.
    :param request: view request
    :retrun: rendered view
    """
    r = requests.get("http://193.142.112.220:8337/companyList")
    company_data = r.json()
    return render(request, 'recrut/company.html', {"data": company_data})


@login_required
def materials(request):
    """
    This view is responsible for show materials.
    :param request: view request
    :retrun: rendered view
    """
    r = requests.get("http://193.142.112.220:8337/materialList")
    material_data = r.json()
    return render(request, 'recrut/material.html', {"data": material_data})


@login_required
def company_assigned(request, company_id):
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
    company_assigned_data = r.json()
    return render(request, 'recrut/material.html', {
        "data": company_assigned_data})


@login_required
def material_detail(request, _id):
    """
    This view is responsible for show materials details.
    :param request: view request
    :retrun: rendered view
    """
    r = requests.get(
        "http://193.142.112.220:8337/materialDetails",
        params={"ID": _id}
    )
    material_detail_data = r.json()
    return render(request, 'recrut/material_details.html', {
        "data": material_detail_data})
