from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import generic

from .forms import CreateAccount
from .models import Account


# Create your views here.
class AccountCreation(generic.CreateView):
    model = Account
    template_name = 'MedRec/form.html'
    form_class = CreateAccount

    def post(self, request, *args, **kwargs):
        pass
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            position = form.cleaned_data['position']
            user_group = Group.objects.get(name=position)
            user.groups.add(user_group)
            user_group_default = Group.objects.get(name='Users')
            user.groups.add(user_group_default)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            acct = Account(
                User=user,
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                position=position
            )
            acct.save()
            return redirect('MedRec:index')
        else:
            return render(request, self.template_name, {'form': form})


class AllAccountsList(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    template_name = 'MedRec/index.html'
    context_object_name = 'Account_list'

    def get_queryset(self):
        return Account.objects.all()
