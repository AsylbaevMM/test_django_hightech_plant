from django.shortcuts import render
from .models import MyUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def user_list(request):
    users_list = MyUser.objects.all().order_by('date_joined')
    # Постраничная разбивка с 5 пользователями на страницу
    paginator = Paginator(users_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        users = paginator.page(page_number)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,
                  'users_list.html',
                  {'users': users})


