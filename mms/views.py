from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


# Create your views here.


@api_view(['GET'])
def router(request):
    routes = [
        'api/',
        'api/students/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def total_students(request):
    students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def students(request, mess):
    try:
        students = Student.objects.filter(mess__mess_name=mess)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    except:
        return Response("No student found", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def student(request, username):
    try:
        student = Student.objects.get(account__username=username)

        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET'])
def room(request, username):
    try:
        student = Student.objects.get(account__username=username)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET'])
def rooms(request, mess):
    try:
        students = Student.objects.filter(mess__mess_name = mess)
        rooms = [student.room_num for student in students]
        return Response(rooms)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def room(request, room_number):
    try:
        students = Student.objects.filter(room_num=room_number)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    except:
        return Response()


@api_view(['GET', 'POST'])
def student_form(request, username):
    if request.method == "POST":
        mess = request.data['mess']
        room = request.data["room"]
        nid = request.data["nid"]
        phone = request.data["phone"]
        dept = request.data["dept"]
        district = request.data["district"]
        division = request.data["division"]

        account = User.objects.get(username=username)
        mess_ = Mess.objects.get(mess_name=mess)

        student_form = Student.objects.create(
            mess=mess_,
            account=account,
            room_num=room,
            nid=nid,
            phone=phone,
            dept=dept,
            district=district,
            division=division
        )
        student_form.save()

        students = Student.objects.filter(room_number=room)
        if len(students)>=3:
            return Response("Already 3 members have in this room, please select another room.")
                
      
        return Response("Success")
    return Response("")


@api_view(['GET'])
def payments(request, mess):
    pay = Payment.objects.filter(student__mess__mess_name=mess)
    serializer = PaymentSerializer(pay, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def make_payment(request):
    try:
        if request.method == "POST":
            username = request.data['username']
            tk = request.data['tk']
            month = request.data['month']
            student = Student.objects.get(account__username=username)
            Payment.objects.create(student=student, month=month, tk=tk, is_paid=False).save()
            return Response(f"Successfully send {tk}tk")

    except:
        return Response("")


@api_view(['GET'])
def payment_history(request, username):
    try:
        payment = Payment.objects.filter(student__account__username=username)

        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)
    except:
        return Response("No Payment History")


@api_view(['GET', 'POST'])
def payment_confirmation_list(request, id):
    mess = request.data.get('mess')
    pay = Payment.objects.filter(student__mess__mess_name=mess)
    serializer = PaymentSerializer(pay, many=True)

    if request.method == "POST":

        payment_confirmation = Payment.objects.get(id=id)

        username = payment_confirmation.username

        payment_confirmation.is_paid=True
        payment_confirmation.save()

        return Response(f"{username} payment confirmed")

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def payment_confirmation(request, mess):

    pay = Payment.objects.filter(student__mess__mess_name=mess).filter(is_paid=False)
    serializer = PaymentSerializer(pay, many=True)

    if request.method == "POST":
        id = request.data['id']
        username = request.data['username']

        payment_confirmation = Payment.objects.get(id=id)

        month = payment_confirmation.month
        print(month)
        tk = payment_confirmation.tk
        print(tk)
        email = User.objects.get(username=username).email
        print(email)

        subject = f"{month} Month Mess Bill Payment Confirmation"
        message = f'Hi {username}, \nYour {month} month bill {tk} tk is confirm.\nThanks\nBMS'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]

        send_mail(subject, message, email_from, recipient_list)

        payment_confirmation.is_paid = True
        payment_confirmation.save()

        return Response(f"{username}'s {payment_confirmation.month} payment confirmed")

    return Response(serializer.data)


@api_view(['GET'])
def leave_request(request, username):
    try:
        student = Student.objects.get(account__username=username)
        student.sts = "leaving"
        student.save()
        return Response("Leaving")

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def edit_info(request, username):
    if request.method=="PUT":
        name = request.data['username']
        mess = request.data['mess']
        room_num = request.data['room']
        nid = request.data['nid']
        phone = request.data['phone']
        email = request.data['email']
        dept = request.data['dept']
        district = request.data['district']
        division = request.data['division']
        sts = request.data['sts']

        user = User.objects.get(username=username)
        user.username=name
        user.email=email
        user.save()

        mess = Mess.objects.get(mess_name=mess)
        student = Student.objects.get(account__username=username)

        student.account=user
        student.mess=mess
        student.room_num=room_num
        student.nid = nid
        student.phone = phone
        student.dept = dept
        student.district = district
        student.division = division
        student.sts=sts
        student.save()

        return Response("Updated")

    return Response("")

