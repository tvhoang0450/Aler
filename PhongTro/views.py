from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import decorators, authenticate, login
from django.views import View
from .models import PhongTro

from .forms import PhongTroForm
from .filters import PhongTroFilter
from HuyenQuan.models import HuyenQuan


def index(request):
    return HttpResponse("Xin chào")


# Create your views here.
class save_news_class(LoginRequiredMixin, View):
    login_url = '/NguoiDung/login/'

    def get(self, request):
        a = PhongTroForm()
        return render(request, 'homepage/PhongTro/property-submit.html', {'f': a})

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
    tinhtp_id = request.GET.get('TinhTP')
    quanhuyens = HuyenQuan.objects.filter(TinhTP_id=tinhtp_id).order_by('TenHuyen')
    print(quanhuyens)
    print(tinhtp_id)
    return render(request, 'homepage/PhongTro/loadhuyen.html', {'quanhuyens': quanhuyens})
