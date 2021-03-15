from django.shortcuts import render

# Create your views here.
from django.views import View

from PhongTro.models import PhongTro
from PhongTro.filters import PhongTroFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Home(View):
    def get(self, request):
        list = PhongTro.objects.all()
        phongtro_filter = PhongTroFilter(request.GET, queryset=list)

        # Paging
        # paginator = Paginator(list, 2)
        paginator = Paginator(phongtro_filter.qs, 6)
        page = request.GET.get('page', 1)
        try:
            orders_paged = paginator.page(page)
        except PageNotAnInteger:
            orders_paged = paginator.page(1)
        except EmptyPage:
            orders_paged = paginator.page(paginator.num_pages)

        context = {
            'form': phongtro_filter.form,
            'PhongTros': phongtro_filter.qs,
            "orders": orders_paged,
            'list': list
        }

        return render(request, 'homepage/index.html', context)



class About(View):
    def get(self, request):
        return render(request, 'homepage/about.html')

class Contact(View):
    def get(self, request):
        return render(request, 'homepage/contact.html')

class HuongDan(View):
    def get(self, request):
        return render(request, 'homepage/huongdan.html')
