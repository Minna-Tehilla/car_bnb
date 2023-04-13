# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from .models import ContactMessage, Car, Person, Rent, Bike, User, Factory
from .serializers import MessageSerializer, CarSerializer, PersonSerializer, RentSerializer, BikeSerializer, \
    FactorySerializer


@api_view (['GET', 'POST', 'PUT', 'DELETE'])
def serve_messages(request):
    try:
        if request.method == 'GET':
            if "message_id" in request.query_params:
                message_id = request.query_params.get ("message_id")
                message = ContactMessage.objects.get (pk = message_id)
                ms = MessageSerializer (message)
                return Response (ms.data)
            else:
                messages = ContactMessage.objects.all ()
                ms = MessageSerializer (messages, many = True)
                return Response (ms.data)

        elif request.method == "POST":
            ms = MessageSerializer (data = request.data)
            if ms.is_valid ():
                ms.save ()
                return Response ("Object Created")
            else:

                return Response ({"Error": ms.errors})
        elif request.method == 'PUT':
            message_id = request.query_params.get ("message_id")
            message_instance = ContactMessage.objects.get (pk = message_id)
            ms = MessageSerializer (data = request.data, instance = message_instance)
            if ms.is_valid ():
                ms.save ()  # did I make an update method where?
                return Response ("Object updated")
            else:
                return Response ({"Error": ms.errors}, status = 400)
        else:
            message_id = request.query_params.get ("message_id")
            message_instance = ContactMessage.objects.get (pk = message_id)
            message_instance.delete ()
            return Response ("Object deleted")

    except Exception as e:
        return Response (f"Unknown error:{e}")


@api_view (['GET', 'POST', 'PUT', 'DELETE'])
class CarApi (APIView):

    @classmethod
    def get(cls, request):
        try:
            if "car_id" in request.query_params:
                car_id = request.query_params.get ("car_id")
                # car = Car.objects.get (plate_number = car_id)
                car = Car.objects.get (pk = car_id)
                cs = CarSerializer (car)
                return Response (cs.data)
            else:
                cars = Car.objects.all ()
                cs = CarSerializer (cars, many = True)
                return Response (cs.data)
        except Exception as e:
            return Response (f"Error: {e}")

    @classmethod
    def post(cls, request):
        cs = CarSerializer (data = request.data)
        if cs.is_valid ():
            cs.save ()  # do i need a create method here or in serializers?
            return Response ("Car object created successfully!!")
        else:
            return Response ({"Error": cs.errors})

    @classmethod
    def put(cls, request):
        car_id = request.query_params.get ("car_id")
        # car_instance = Car.objects.get (plate_number = car_id)
        car_instance = Car.objects.get (pk = car_id)

        cs = CarSerializer (data = request.data, instance = car_instance)
        if cs.is_valid ():
            cs.save ()  # do i need a create method here or in serializers?
            return Response ("Car object updated successfully!!")
        else:
            return Response ({"Error": cs.errors}, status = 400)

    @classmethod
    def delete(cls, request):
        car_id = request.query_params.get ("car_id")
        # car_instance = Car.objects.get (plate_number = car_id)
        car_instance = Car.objects.get (pk = car_id)
        car_instance.delete ()
        return Response ("Object deleted")

    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == 'GET' and not self.action == 'get':
    #         return HttpResponse("incorrect method (GET)", 400)
    #
    #     if request.method == 'POST' and not self.action == 'post':
    #         return HttpResponse("incorrect method (POST)", 400)
    #
    #     if request.method == 'PUT' and not self.action == 'put':
    #         return HttpResponse ("incorrect method (PUT)", 400)
    #
    #     if request.method == 'DELETE' and not self.action == 'delete':
    #         return HttpResponse ("incorrect method (DELETE)", 400)
    #
    #     return super().dispatch(request, *args, **kwargs)


class PersonApi (APIView):
    @classmethod
    def get(cls, request):
        try:
            if "person_id" in request.query_params:
                person_id = request.query_params.get ("person_id")

                person = Person.objects.get (pk = person_id)
                ps = PersonSerializer (person)
                return Response (ps.data)
            else:
                people = Person.objects.all ()
                ps = PersonSerializer (people, many = True)
                return Response (ps.data)
        except Exception as e:
            return Response (f"Error: {e}")

    @classmethod
    def post(cls, request):
        ps = PersonSerializer (data = request.data)
        if ps.is_valid ():
            ps.save ()  # do i need a create method here or in serializers?
            return Response ("Person object created successfully!!")
        else:
            return Response ({"Error": ps.errors})

    @classmethod
    def put(cls, request):
        person_id = request.query_params.get ("person_id")
        person_instance = Person.objects.get (pk = person_id)

        ps = PersonSerializer (data = request.data, instance = person_instance)
        if ps.is_valid ():
            ps.save ()  # do i need a create method here or in serializers?
            return Response ("Person object updated successfully!!")
        else:
            return Response ({"Error": ps.errors}, status = 400)

    @classmethod
    def delete(cls, request):
        person_id = request.query_params.get ("person_id")
        person_instance = Person.objects.get (pk = person_id)
        person_instance.delete ()
        return Response ("Object deleted")


class RentApi (APIView):
    @classmethod
    def get(cls, request):
        try:
            if "rent_id" in request.query_params:
                rent_id = request.query_params.get ("rent_id")

                rent = Rent.objects.get (pk = rent_id)
                rs = RentSerializer (rent)
                return Response (rs.data)
            else:
                rents = Rent.objects.all ()
                rs = RentSerializer (rents, many = True)
                return Response (rs.data)
        except Exception as e:
            return Response (f"Error: {e}")

    @classmethod
    def post(cls, request):
        rs = RentSerializer (data = request.data)
        if rs.is_valid ():
            rs.save ()  # do i need a create method here or in serializers?
            return Response ("Rent object created successfully!!")
        else:
            return Response ({"Error": rs.errors})

    @classmethod
    def put(cls, request):
        rent_id = request.query_params.get ("rent_id")
        rent_instance = Rent.objects.get (pk = rent_id)

        rs = RentSerializer (data = request.data, instance = rent_instance)
        if rs.is_valid ():
            rs.save ()  # do i need a create method here or in serializers?
            return Response ("Rent object updated successfully!!")
        else:
            return Response ({"Error": rs.errors}, status = 400)

    @classmethod
    def delete(cls, request):
        rent_id = request.query_params.get ("rent_id")
        rent_instance = Person.objects.get (pk = rent_id)
        rent_instance.delete ()
        return Response ("Object deleted")


@api_view (['POST'])
def signup(request):
    print(request)
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get('email', None)

    user = User.objects.create_user (username = username, password = password, email = email)
    token = Token.objects.create(user=user)
    return Response ({'message': f"new user created. id:{user.id}, name:{user.username}. token: {token}",
                      "token": str(token)})


@api_view (['GET'])
@authentication_classes ([BasicAuthentication, TokenAuthentication])
@permission_classes ([IsAuthenticated])
def private(request):
    return Response (f"This is a private response. User is: {request.user.username}")


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def bike(request):
    try:
        match request.method:
            case 'POST':
                factory = Factory.objects.get (id = request.data['factoryId'])
                bike_serializer = BikeSerializer (instance = factory, data = request.data)
                if bike_serializer.is_valid ():
                    BikeSerializer.save ()
                    return Response (
                        status = status.HTTP_201_CREATED,
                        data = {
                            "status": 'success',
                            'message': 'bike has been created',
                            'bike': bike_serializer.data
                        }
                    )
                else:
                    return Response (
                        status = status.HTTP_400_BAD_REQUEST,
                        data = {
                            'status': 'fail',
                            'message': 'the data provided is incorrect',
                            'error': bike_serializer.errors
                        }
                    )
            case 'GET':
                bikes = Bike.objects.all ()
                bikes_json = BikeSerializer (bikes, many = True)
                return Response (
                    status = status.HTTP_200_OK,
                    data = {
                        'status': 'success',
                        'message': 'retrieved all bikes',
                        'bikes': bikes_json
                    }
                )
            case _:
                return Response (
                    status = status.HTTP_400_BAD_REQUEST,
                    data = {
                        'status': 'fail',
                        'message': f'the method {request.method} is not allowed for this url'
                    }
                )

    except Exception as ex:
        print (ex)
        return Response (
            status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            data = {
                'status': 'fail',
                'message': 'a server error was thrown',
                'error': str(ex)
            }
        )

@api_view(['GET'])
def home(request):
    return Response("Test passed!!!")