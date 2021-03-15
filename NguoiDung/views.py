from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

# Create your views here.
from django.views import View
from django.views.generic import UpdateView

from .models import NguoiDung
from .forms import NguoiDungForm
from .models import NguoiDung
from PhongTro.models import PhongTro


class LoginClass(View):
    def get(self, request):
        return render(request, 'NguoiDung/login.html')

    def post(self, request):
        tk = request.POST.get('username')
        mk = request.POST.get('password')
        my_user = authenticate(username=tk, password=mk)
        if my_user is None:
            return HttpResponse('User không tồn tại, Đăng nhập thất bại')
        login(request, my_user)
        return redirect('/', {'username': tk})


class RegisterClass(View):
    def get(self, request):
        a = NguoiDungForm()
        return render(request, 'NguoiDung/register.html', {'f': a})

    def post(self, request):
        nd = NguoiDungForm(request.POST)
        if nd.is_valid():
            nd.save()
            return redirect('/NguoiDung/login')
        else:
            return HttpResponse('Dwx liệu không validate')


class ProfileClass(View):
    def get(self, request, **kwargs):
        a = self.request.GET.get('id')
        user_id = self.request.user
        dsach_tin_dang = PhongTro.objects.filter(NguoiDung_id=user_id)
        return render(request, 'NguoiDung/profile.html', {'dsach_tin_dang': dsach_tin_dang})


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = NguoiDung.objects.get(id=id)
    context["dsach_tin_dang"] = PhongTro.objects.filter(NguoiDung_id=id)
    return render(request, "NguoiDung/profile.html", context)


# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(NguoiDung, id=id)

    # pass the object as instance in form
    form = NguoiDung(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return render(request, "NguoiDung/update.html", context)
