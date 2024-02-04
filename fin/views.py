import csv
import os
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from fin.forms import *
from fin.models import Revenue, Profile, BankAccount, Ledger
from Account.models import User

import json
from django.conf import settings
from django.http import Http404, HttpResponse
from fin.utils import get_transfer, get_transaction, account_id_generator
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def home(request):
    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()
    context = get_transaction(request)

    context.update({'ledger_count': ledger_count})

    return render(request, 'fin/index.html', context)


def transfer(request):
    get_transfer(request)

    gas_fee = Revenue.objects.get(id=1).gas_fee

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/transfer.html', {'count': count,
                                             "gas_fee": gas_fee, 'ledger_count': ledger_count})


def friend_transfer(request, account_id):
    get_transfer(request)

    gas_fee = Revenue.objects.get(id=1).gas_fee

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'account_id': account_id, 'count': count,
               'gas_fee': gas_fee, 'ledger_count': ledger_count}
    return render(request, 'fin/friend-transfer.html', context)


def transaction(request):
    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = get_transaction(request)
    context.update({'ledger_count': ledger_count})

    csv_file = open(
        'static/files/Transactions-{}.csv'.format(request.user.username), 'w', newline='')
    writter = csv.writer(csv_file)
    writter.writerow(
        ['Sender', 'Receiver', 'Amount', 'Transaction ID', 'Time'])
    for transaction in context['transactions']:
        sender = transaction.sender
        receiver = transaction.receiver
        amount = transaction.amount
        transaction_id = transaction.transaction_id
        time = transaction.time

        print(sender, receiver, amount, transaction_id, time)

        row = [sender, receiver, amount, transaction_id, time]
        writter.writerow(row)

    csv_file.close()

    return render(request, 'fin/transaction.html', context)


def ledger(request):
    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    data = get_transaction(request)
    count = data['count']
    no_ledger = ''

    csv_file = open('static/files/ledger.csv', 'w', newline='')
    writter = csv.writer(csv_file)
    writter.writerow(
        ['Sender', 'Receiver', 'Amount', 'Transaction ID', 'Time'])
    for ledger in ledgers:
        sender = ledger.sender
        receiver = ledger.receiver
        amount = ledger.amount
        transaction_id = ledger.transaction_id
        time = ledger.time

        print(sender, receiver, amount, transaction_id, time)

        row = [sender, receiver, amount, transaction_id, time]
        writter.writerow(row)

    csv_file.close()

    if not ledgers:
        no_ledger = 'No Ledger Found'

    context = {'ledgers': ledgers, 'ledger_count': ledger_count,
               'count': count, 'no_ledger': no_ledger}
    return render(request, 'fin/ledger.html', context)


def balance(request, username):

    try:
        user = User.objects.get(username=username)
        balance = BankAccount.objects.get(user=user).balance
    except:
        balance = 0

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'balance': balance, 'count': count,
               'ledger_count': ledger_count}
    return render(request, 'fin/balance.html', context)


def friends(request):

    accounts = BankAccount.objects.all()
    accounts = BankAccount.objects.exclude(user=request.user)

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'accounts': accounts, 'count': count,
               'ledger_count': ledger_count}
    return render(request, 'fin/friends.html', context)


def profile(request, username):

    user = User.objects.get(username=username)
    try:
        previous_bank_account = BankAccount.objects.get(user=user)
    except:
        previous_bank_account = ''
        messages.info(
            request, 'Hello Mr. {}, you have no bank account.'.format(username))
        return render(request, 'fin/profile.html')

    try:
        user = User.objects.get(username=username)
    except:
        user = ''
        messages.info(request, 'No User Details Show')

    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = ''
        messages.info(request, 'No Profile Details Show')

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'previous_bank_account': previous_bank_account,
               'user': user, 'profile': profile, 'username': username,
               'count': count, 'ledger_count': ledger_count}
    return render(request, 'fin/profile.html', context)


def bank_account(request):
    print(request.user)
    if request.method == "POST":
        account_id = request.POST['account_id']
        balance = request.POST['balance']

        bank_account = BankAccount.objects.create(
            user=request.user,
            account_id=account_id,
            balance=balance
        )

        bank_account.save()
        messages.info(
            request, 'Hey ! Mr. {}, Your bank account successfully created.'.format(request.user.username))
        return redirect('profile', username=request.user.username)

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/bank-account.html', {'count': count,
                                                 'account_id': account_id_generator(), 'ledger_count': ledger_count})


def setting(request):

    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/setting.html', {'count': count, 'profile': profile, 'ledger_count': ledger_count})


def edit_user(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        

        user.name = request.POST['name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()


    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'user': user, 'count': count, 'ledger_count': ledger_count}
    return render(request, 'fin/edit-user.html', context)


def add_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        profile = Profile.objects.create(
            user=request.user,
            address=request.POST.get('address'),
            bio=request.POST.get('bio')
        )
        profile.save()
        return redirect('profile', username=request.user.username)

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/edit-profile.html', {'form': form, 'count': count, 'ledger_count': ledger_count})


def edit_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'count': count, 'ledger_count': ledger_count,
               'form': form, 'profile': profile}
    return render(request, 'fin/edit-profile.html', context)


def log_in(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('fin-home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not existed')

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('fin-home')
        else:
            messages.error(request, 'Username or password does not exist')

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'page': page, 'count': count, 'ledger_count': ledger_count}
    return render(request, 'fin/login.html', context)


def signup(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('fin-home')
        else:
            messages.error(request, 'Error in Registration !!!')

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    context = {'form': form, 'count': count, 'ledger_count': ledger_count}
    return render(request, 'fin/signup.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


def developer(request):

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/developer.html', {'count': count, 'ledger_count': ledger_count})


@login_required
@permission_required('is-superuser')
def gas_fee_update(request):
    revenue = Revenue.objects.get(id=1)

    previous_gas_fee = revenue.gas_fee
    if request.method == "POST":
        updated_gas_fee = request.POST['gas_fee']

        revenue.gas_fee = updated_gas_fee
        revenue.save()
        return redirect('fin-home')

    data = get_transaction(request)
    count = data['count']

    ledgers = Ledger.objects.all()
    ledger_count = ledgers.count()

    return render(request, 'fin/update-gas-fee.html', {'previous_gas_fee': previous_gas_fee,
                                                   'count': count,
                                                   'ledger_count': ledger_count})
