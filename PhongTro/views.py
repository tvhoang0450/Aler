from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import decorators, authenticate, login
from django.views import View
from .models import PhongTro

from .forms import PhongTroForm
from .filters import PhongTroFilter
from DiaChi.models import district, province, ward, street


def index(request):
    return HttpResponse("Xin chào")


# Create your views here.
class save_news_class(LoginRequiredMixin, View):
    login_url = '/NguoiDung/login/'

    def get(self, request):
        a = PhongTroForm()
        #return render(request, 'homepage/PhongTro/property-submit.html', {'f': a})
        return render(request, 'homepage/PhongTro/add.html', {'f': a})

    def post(self, request):
        g = PhongTroForm(request.POST, request.FILES)
        if g.is_valid():
            g.save()
            return HttpResponse(g)
        else:
            return HttpResponse("Không lưu được validate")


class getAll(View):
    def get(self, request):
        a = PhongTroForm()
        return render(request, 'homepage/index.html', {'f': a})

    def post(self, request):
        g = PhongTroForm(request.POST, request.FILES)
        if g.is_valid():
            g.save()
            return HttpResponse(g)
        else:
            return HttpResponse("Không lưu được validate")


class getdetail(View):
    def get(self, request, PhongTro_id):
        p = PhongTro.objects.get(pk=PhongTro_id)
        return HttpResponse(p)


def load_huyen(request):
    tinhtp_id = request.GET.get('province')
    districts = district.objects.filter(_province_id=tinhtp_id).order_by('_name')
    return render(request, 'homepage/PhongTro/loadhuyen.html', {'districts': districts})


def load_xa(request):
    tinhtp_id = request.GET.get('district')
    wards = ward.objects.filter(_district_id=tinhtp_id).order_by('_name')
    return render(request, 'homepage/PhongTro/loadxa.html', {'wards': wards})


def load_duong(request):
    tinhtp_id = request.GET.get('district')
    print(tinhtp_id)
    streets = street.objects.filter(_district_id=tinhtp_id).order_by('_name')
    return render(request, 'homepage/PhongTro/loadduong.html', {'streets': streets})
