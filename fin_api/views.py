from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from fin.forms import CustomUserForm

from fin_api.serializers import *
from django.contrib import messages
from fin.models import Ledger, Revenue, User, Transfer, BankAccount, Profile
from fin.utils import get_transaction, get_transfer, transaction_id_generator
from django.contrib.auth import authenticate, login, logout
import json
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework import generics, permissions, mixins
from fin_api.serializers import SignUpSerializer, UserSerializer


def getRouter(request):
    data = {
        "content": "Welcome to Fin API"
    }
    return JsonResponse(data)


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        user = None
        if not user:
            user = authenticate(username=username, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username, 'token': token.key}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response()


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)

        user = None
        if not user:
            user = authenticate(username=username, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username, 'token': token.key}, status=status.HTTP_200_OK)

        return Response('Invalid Credintial', status=status.HTTP_401_UNAUTHORIZED)
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == "POST":
        try:
            request.user.authtoken_token.delete()
            return Response({'message': 'Successfully Log Out'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'erroe': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def transfer(request):
    if request.method == "POST":
        account_id = request.data['account_id']
        amount = request.data['amount']
        sender = request.data['sender']
        print(account_id, amount)

        sender_acc = User.objects.get(username=sender)

        revenues = Revenue.objects.get(id=1)
        gas_fee = revenues.gas_fee
        service_charge = float(amount) * (gas_fee / 100)

        try:
            receiver_account = BankAccount.objects.get(
                account_id=account_id)
            receiver = receiver_account.user.username
            sender_account = BankAccount.objects.get(user=sender_acc)
           

            # balance system
            try:
                if sender_account.balance > float(amount) + float(service_charge):
                    sender_account.balance = sender_account.balance - float(amount) - float(service_charge)

                    receiver_account.balance = receiver_account.balance + float(amount)

                    sender_account.save()
                    receiver_account.save()

                    revenues.revenue += float(service_charge)
                    transfer = Transfer.objects.create(account_id=account_id, amount=amount)

                    transfer.save()

                    ledger = Ledger.objects.create(sender=sender_account.user.username,
                                                receiver=receiver_account.user.username,
                                                amount=amount,
                                                transaction_id=transaction_id_generator())

                    ledger.save()
                    revenues.save()

                    return Response('You successfully sent {}$ to {}.'.format(amount, receiver))
                else:
                    return Response('Account Balance is insufficient')

            except:
                return Response('There are some issues')

        except:
            return Response('No User Found')

    return Response()


@api_view(['GET'])
def transaction(request, username):
    transactions = Ledger.objects.filter(
        sender=username) | Ledger.objects.filter(receiver=username)

    serializer = LedgerSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ledger(request):
    ledgers = Ledger.objects.all()

    serializer = LedgerSerializer(ledgers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def balance(request, username):
    try:
        user = User.objects.get(username=username)
        balance = BankAccount.objects.get(user=user).balance
    except:
        balance = 0

    return Response({'balance': balance})


@api_view(['GET'])
def people(request, username):
    user = User.objects.get(username=username)
    accounts = BankAccount.objects.all().exclude(user=user)
    serializer = BankAccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_user(request):
    accounts = BankAccount.objects.all()
    serializer = BankAccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_bank_account(request):
    if request.method == "POST":
        account_id = request.data['account_id']
        balance = request.data['balance']
        username = request.data['username']

        user = User.objects.get(username=username)

        BankAccount.objects.create(
            user=user,
            account_id=account_id,
            balance=balance
        )

        return Response("Bank Account Created")

    return Response()


@api_view(['GET'])
def get_bank_account(request, username):
    try:
        user = User.objects.get(username=username)
        account = BankAccount.objects.get(user=user)
        serializer = BankAccountSerializer(account, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET'])
def find_bank_account(request, id):
    try:
        account = BankAccount.objects.get(account_id=id)
        serializer = BankAccountSerializer(account, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET'])
def verify_bank_account(request, id):
    try:
        account = BankAccount.objects.get(account_id=id)
        serializer = BankAccountSerializer(account, many=False)
        return Response("Already Existed")
    except:
        if len(str(id)) >= 8:
            return Response("Verified")
        else:
            return Response("Writting...")


@api_view(['GET'])
def user_info(request, username):
    user = User.objects.get(username=username)
    serializer = AccountSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_profile(request):
    if request.method == "POST":
        address = request.data['address']
        bio = request.data['bio']

        Profile.objects.create(user=request.user, address=address, bio=bio)

    return Response('Profile Created')


@api_view(['GET'])
def get_profile(request, username):
    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = ''

    profile_serializer = ProfileSerializer(profile)
    return Response(profile_serializer.data)


@api_view(['GET'])
def revenue(request):
    try:
        revenue = Revenue.objects.all()[0]
        serializer = RevenueSerializer(revenue, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET', 'POST'])
def create_gas_fee(request):
    if request.method == "POST":
        gas_fee = request.data['gas_fee']

        gas = Revenue.objects.create(gas_fee=gas_fee, revenue=0)
        gas.save()

        return Response("Gas Fee Successfully Created")

    return Response("")


@api_view(['GET', 'PUT'])
def update_gas_fee(request):
    if request.method == "PUT":
        gas_fee = request.data['gas_fee']
        gas = Revenue.objects.get(id=1)
        gas.gas_fee = gas_fee
        gas.save()
        return Response("Gas Fee Successfully Updated")

    return Response("")
