from django.shortcuts import render
from .models import MyUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import get_user_model

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
    profile = get_object_or_404(MyUser, id=user_id)

    return render(request,
                  'user_detail.html',
                  {'profile': profile})



