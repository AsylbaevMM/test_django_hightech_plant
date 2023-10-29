from django.shortcuts import render
from .models import MyUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm, UpdateUserForm, ChangeEmailForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from test_django_hightech_plant.settings import EMAIL_HOST_USER
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from test_django_hightech_plant.settings import DOMAIN


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


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    initial = None  # принимает {'key': 'value'}
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        # перенаправит на домашнюю страницу, если пользователь попытается получить доступ к странице регистрации после авторизации
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'{username}, ссылка на подтверждение регистрации отправлена на {email}')
            user = MyUser.objects.all().filter(email=email).first()
            send_mail('Код подтверждения',
                      f"Подтвердите регистрацию: http://{DOMAIN}/activate/{user.id}/",
                      EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return redirect(to='login') # редирект на страницу логина после регистрации

        return render(request, self.template_name, {'form': form})


def activate(request, user_id):
    if not request.user.is_authenticated:
        user = get_object_or_404(MyUser, id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, 'Аккаунт активирован')
        return redirect(to='login')

    return redirect(to='user_list')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('accounts:user_list')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='accounts:users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'registration/profile.html', {'user_form': user_form})


def change_email_done(request, old_email, new_email):
    if request.user.is_authenticated:
        if request.user.email == old_email:
            user = request.user
            user.email = new_email
            user.save()
            messages.success(request, f'Ваш email изменен на {new_email}')
        else:
            messages.error(request, f'Ошибка смены email')
        return redirect(to='accounts:users-profile')
    return redirect(to='login')


def change_email(request):
    if request.method == 'POST':
        # Форма была передана на обработку
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            new_email = cd['email']
            matches = MyUser.objects.all().filter(email=new_email)
            if not matches:
                send_mail('Смена адреса электронной почты',
                          f"Подтвердите смену почты на {new_email}: http://{DOMAIN}/change_email_done/{request.user.email}/{new_email}/",
                          EMAIL_HOST_USER,
                          [request.user.email],
                          fail_silently=False)
                messages.success(request, f'Подтверждение смены email отправлено на {request.user.email}')
                return redirect(to='accounts:users-profile')
            messages.error(request, f'Данный email уже используется')
    else:
        form = ChangeEmailForm()
    return render(request, 'registration/change_email.html', {'change_email_form': form})