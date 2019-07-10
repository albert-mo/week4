from django.core.paginator import Paginator
from django.shortcuts import render
from django_web.models import GoodInfo
# Create your views here.


def index(request):
    limit = 4
    good_info = GoodInfo.objects[:100]
    paginator = Paginator(good_info, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'GoodInfo': loaded
    }
    return render(request, 'index.html', context)
