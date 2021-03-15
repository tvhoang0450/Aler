from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from DiaChi.models import district, ward, street
from .forms import PhongTroForm, ImageForm
from .models import PhongTro, Images


def index(request):
    return HttpResponse("Xin chào")

    # Create your views here.


# class save_news_class(LoginRequiredMixin, View):
#     login_url = '/NguoiDung/login/'
#
#     def get(self, request):
#         a = PhongTroForm()
#         return render(request, 'homepage/PhongTro/add.html', {'f': a})
#
#
#     def post(self, request):
#         g = PhongTroForm(request.POST, request.FILES)
#         if g.is_valid():
#             g.save()
#             return HttpResponse(g)
#         else:
#             return HttpResponse("Không lưu được validate")


def post(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        form = PhongTroForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.NguoiDung = request.user
            post.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(phongtro=post, image=image)
                photo.save()
            messages.success(request, "Posted!")
            return HttpResponseRedirect("/")
        else:
            print(form.errors, formset.errors)
    else:
        form = PhongTroForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'homepage/PhongTro/add.html',
                  {'postForm': form, 'formset': formset})
    # return render(request, 'homepage/PhongTro/property-submit.html',
    #               {'postForm': form, 'formset': formset})


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


class PhongTroUpdate(UpdateView):
    model = PhongTro
    fields = (
        'DichVu', 'TieuDe', 'province', 'district', 'ward', 'street', 'Gia', 'SDT',
        'NoiDung', 'DienTich', 'Anh')
    success_url = reverse_lazy('core:index')


class getdetail(View):
    def get(self, request, PhongTro_id):
        p = PhongTro.objects.get(pk=PhongTro_id)
        return render(request, 'homepage/property-details.html', {'p': p})


class PhongTroDelete(DeleteView):
    model = PhongTro
    # success_url = reverse_lazy('NguoiDung:profile')
    success_url = "/NguoiDung/profile/{NguoiDung_id}"


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
