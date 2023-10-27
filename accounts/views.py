from django.shortcuts import render
from .models import MyUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect



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


def user_detail(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)

    return render(request,
                  'user_detail.html',
                  {'user': user})
