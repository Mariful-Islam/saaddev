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


        try:
            global mess
            mess = Student.objects.get(account__username=username).mess.mess_name

        except:
            mess = Mess.objects.get(owner=username).mess_name



        user = None
        if not user:
            user = authenticate(username=username, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username, 'token': token.key, 'mess': mess}, status=status.HTTP_200_OK)

        return Response('Invalid Credintial')
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
def total_students(request):
    students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def students(request):
    if request.method == "POST":
        mess = request.data['mess']

        students = Student.objects.filter(mess__mess_name=mess)

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    return Response('')


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
        account = User.objects.get(username=username)
        student = Student.objects.get(account=account)
        room = Room.objects.get(student=student)

        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    except:
        return Response("")


@api_view(['GET', 'POST'])
def rooms(request):
    if request.method=="POST":
        mess = request.data['mess']

        rooms = Room.objects.filter(student__mess__mess_name=mess).exclude(student__sts="exit")

        room_number = []
        for room in rooms:
            room_number.append(str(room.room_number))

        return Response(room_number)
    return Response("")


@api_view(['GET'])
def room(request, room_number):
    room = Room.objects.filter(room_number=room_number)

    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def floors(request):
    floor_objs = Floor.objects.all()

    serializer = FloorSerializer(floor_objs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def student_form(request):
    if request.method == "POST":
        username = request.data["username"]
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
            nid=nid,
            phone=phone,
            dept=dept,
            district=district,
            division=division
        )
        student = Student.objects.get(account=account)

        try:
            rooms = Room.objects.filter(room_number=room)
            if len(rooms)<3:
                room_ = Room.objects.create(student=student, room_number=room)

            else:
                return Response('Room has 3 of student')
        except:
            room_ = Room.objects.create(student=student, room_number=room)



        Floor.objects.create(
            room=room_,
            student=student,
            number=str(room)[0]
        )

        return Response("Success")
    return Response("")


@api_view(['GET'])
def payments(request):
    pay = Payment.objects.all()
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
            room = Room.objects.get(student__account__username=username)

            Payment.objects.create(student=student, room=room, month=month, tk=tk, is_paid=False).save()


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


@api_view(['GEt', 'PUT'])
def leave_request(request):
    try:
        if request.method == "PUT":
            username = request.data['username']
            student = Student.objects.get(account__username=username)
            student.sts = "leaving"

            student.save()
            return Response("Leaving")

    except:
        return Response("")


@api_view(['GET'])
def username_verification(request, username):
    try:
        user = User.objects.get(username=username)
        return Response("Username Exited Try Another")

    except:
        return Response("Username Verified")


@api_view(['GET', 'PUT'])
def edit_info(request, username):
    if request.method=="PUT":
        name = request.data['username']
        nid = request.data['nid']
        phone = request.data['phone']
        email = request.data['email']
        dept = request.data['dept']
        district = request.data['district']
        division = request.data['division']
        room_num = request.data['room']

        user = User.objects.get(username=username)
        user.username=name

        student = Student.objects.get(account__username=username)

        student.nid = nid
        student.phone = phone
        student.email = email
        student.dept = dept
        student.district = district
        student.division = division


        room = Room.objects.get(student__account__username=username)
        room.room_number = room_num

        floor = Floor.objects.get(student__account__username=username)
        floor.number = str(room_num)[0]

        print(name)
        print(nid)

        return Response("Updated")

    return Response("")

