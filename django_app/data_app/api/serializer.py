from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from data_app.support.regression import nyse_reg, beer_reg
from data_app.models import new_york, beer_review

class NewYorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = new_york
        fields = ['token']
        
class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = beer_review
        fields = ['token']

class NYSEPredictSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = new_york
        fields = ['token', 'company_symbol', 'open_val', 'high_val', 'low_val']
    
    def validate(self, data):
        token = data['token']
        user = Token.objects.filter(key = token)
        print("From Validate", user)
        if not user.exists():
            raise serializers.ValidationError("Please provide a valid token.")
        return data

    def create(self, validated_data):
        token = validated_data['token']
        company_symbol = validated_data['company_symbol']
        open_val = validated_data['open_val']
        high_val = validated_data['high_val']
        low_val = validated_data['low_val']
        company_data = list([company_symbol, open_val, high_val, low_val])
        prediction = nyse_reg(company_data)
        prediction = prediction[-1]

        user_id = Token.objects.filter(key = token).values()[0]["user_id"]

        user = User.objects.get(id = user_id)

        nyse_obj = new_york(
            token = token,
            company_symbol = company_symbol,
            open_val = open_val,
            high_val = high_val,
            low_val = low_val,
            close_prediction = prediction,
            users = user
        )
        print("Before saving")
        nyse_obj.save()
        validated_data['prediction'] = prediction
        return validated_data

class BeerPredictSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = beer_review
        fields = ['token', 'beer_name', 'review_aroma', 'review_pallete', 'review_taste', 'review_appearance', 'beer_abv']
    
    def validate(self, data):
        token = data['token']
        user = Token.objects.filter(key = token)
        print("from validate:", user)
        if not user.exists():
            raise serializers.ValidationError("Please provide a valid token.")
        return data

    def create(self, validated_data):
        token = validated_data['token']
        beer_name = validated_data['beer_name']
        review_aroma = validated_data['review_aroma']
        review_pallete = validated_data['review_pallete']
        review_taste = validated_data['review_taste']
        review_appearance = validated_data['review_appearance']
        beer_abv = validated_data['beer_abv']

        print("Validated Data: ", validated_data)

        company_data = list([review_aroma, review_pallete, review_taste])
        prediction = beer_reg(company_data)
        prediction = prediction[-1]

        user_id = Token.objects.filter(key = token).values()[0]["user_id"]

        user = User.objects.get(id = user_id)
        print("from create:", user)
        beer_obj = beer_review(
            token = token,
            beer_name = beer_name,
            review_aroma = review_aroma,
            review_pallete = review_pallete,
            review_taste = review_taste,
            review_appearance = review_appearance,
            beer_abv = beer_abv,
            prediction_review = prediction,
            users = user
        )
        print("check")
        beer_obj.save()
        return validated_data