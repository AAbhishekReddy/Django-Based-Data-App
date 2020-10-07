from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User

from data_app.api.serializer import NewYorkSerializer, BeerSerializer, NYSEPredictSerializer, BeerPredictSerializer
from data_app.models import new_york, beer_review
from data_app.support.regression import nyse_reg, beer_reg

class NewYorkViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = new_york.objects.all().order_by('-date_time')
    serializer_class = NewYorkSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = NewYorkSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            try:
                token = data['token']
                user_id = Token.objects.filter(key = token).values()[0]["user_id"]

                user = User.objects.get(id = user_id)
                predictions = new_york.objects.filter(users = user).values()
                
                return Response(predictions, status = HTTP_200_OK)
            except KeyError as e:
                return Response({"message":"Please enter the token to view the predictions"}, status = HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

class BeerViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = beer_review.objects.all().order_by('-date_time')
    serializer_class = BeerSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = BeerSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            try:
                token = data['token']
                user_id = Token.objects.filter(key = token).values()[0]["user_id"]

                user = User.objects.get(id = user_id)
                predictions = beer_review.objects.filter(users = user).values()
                print('predictions:', predictions)
                
                return Response(predictions, status = HTTP_200_OK)
            except KeyError as e:
                return Response({"message":"Please enter the token to view the predictions"}, status = HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, statis = HTTP_400_BAD_REQUEST)


class NYSEPredict(viewsets.ModelViewSet):
    serializer_class = NYSEPredictSerializer
    permission_class = [AllowAny]
    queryset = new_york.objects.all().order_by('-date_time')

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = NYSEPredictSerializer(data = data)
    #     if serializer.is_valid(raise_exception = True):
    #         company_symbol = data['company_symbol']
    #         open_val = data['open_val']
    #         high_val = data['high_val']
    #         low_val = data['low_val']
    #         company_data = list([company_symbol, open_val, high_val, low_val])
    #         prediction = nyse_reg(company_data)
    #         prediction = prediction[-1]
    #         data_cp = {
    #             "message" : "Prediction done.",
    #             "prediction" : prediction
    #         }
            
    #         return Response(data_cp, status = HTTP_200_OK)
    #     return Response(serializer.errors, statis = HTTP_400_BAD_REQUEST)

class BeerPredict(viewsets.ModelViewSet):
    serializer_class = BeerPredictSerializer
    permission_class = [AllowAny]
    queryset = beer_review.objects.all().order_by('-date_time')

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     print(data)
    #     serializer = BeerPredictSerializer(data = data)
    #     if serializer.is_valid(raise_exception = True):
    #         beer_name = data['beer_name']
    #         review_aroma = data['review_aroma']
    #         review_pallete = data['review_pallete']
    #         review_taste = data['review_taste']
    #         review_appearance = data['review_appearance']
    #         beer_abv = data['beer_abv']

    #         company_data = list([review_aroma, review_pallete, review_taste])
    #         prediction = beer_reg(company_data)
    #         prediction = prediction[-1]
    #         data_cp = {
    #             "message" : "Prediction done.",
    #             "prediction" : prediction
    #         }
            
    #         return Response(data_cp, status = HTTP_200_OK)
    #     return Response(serializer.errors, statis = HTTP_400_BAD_REQUEST)

