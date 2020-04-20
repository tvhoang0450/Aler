from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import decorators, authenticate, login
from django.views import View
from .models import PhongTro

from .forms import PhongTroForm
from .filters import PhongTroFilter


def index(request):
    return HttpResponse("Đây là đài tiếng nói Việt Nam")


# Create your views here.
class save_news_class(LoginRequiredMixin, View):
    login_url = '/NguoiDung/login/'

    def get(self, request):
        a = PhongTroForm()
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
        list = PhongTro.objects.all()
        # o1 = PhongTro.objects.get(pk=0)
        # o2 = PhongTro.objects.get(pk=1)
        # o3 = PhongTro.objects.get(pk=2)
        # o4 = PhongTro.objects.get(pk=3)
        # o5 = PhongTro.objects.get(pk=4)
        # o6 = PhongTro.objects.get(pk=5)
        # list = [o1, o2, o3, o4, o5, o6]

        query = PhongTro.objects.all()
        phongtro_filter = PhongTroFilter(request.GET, queryset=query)

        context = {
            'form': phongtro_filter.form,
            'PhongTros': phongtro_filter.qs,
        }

        # return render(request, 'homepage/index.html',
        #               {'form': phongtro_filter.form, 'PhongTros': phongtro_filter.qs, 'list': list})
        return render(request, 'homepage/index.html', context)


class getdetail(View):
    def get(self, request, PhongTro_id):
        p = PhongTro.objects.get(pk=PhongTro_id)
        return HttpResponse(p)
