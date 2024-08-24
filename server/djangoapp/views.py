# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)
# ...


# Create a `registration` view to handle sign up request
@csrf_exempt
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    try:
        # Check if user already exists
        User.objects.get(username=username)
        return JsonResponse({"status": 400, "message":
                             "Username already exists"})
    except User.DoesNotExist:
        # If not, create a new user
        User.objects.create_user(username=username,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name,
                                 email=email)
        logger.debug(f"{username} is a new user")
        return JsonResponse({"status": 201, "message":
                             "User created successfully"})
    except Exception as e:
        logger.error(f"Error in registration: {str(e)}")
        return JsonResponse({"status": 500, "message": "Server error"})


# get car
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if (count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake":
                    car_model.car_make.name})
    return JsonResponse({"CarModels": cars})

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# Update the `get_dealerships` render list of dealerships all by default,
# particular state if state is passed


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    if dealerships is None:
        logger.error("Failed to fetch dealerships from backend")
        return JsonResponse({"status": 500, "message":
                             "Internal Server Error"}, status=500)
    if not dealerships:
        logger.warning(f"No dealerships found for state: {state}")
        return JsonResponse({"status": 404, "message":
                             "No dealerships found"}, status=404)
    logger.info(f"Retrieved {len(dealerships)} dealerships for state: {state}")
    return JsonResponse({"status": 200, "dealers": dealerships})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
def get_dealer_reviews(request, dealer_id):
    # if dealer id has been provided
    if (dealer_id):
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        if reviews is None:
            return JsonResponse({"status": 500, "message":
                                 "Error fetching reviews"}, status=500)
        for review_detail in reviews:
            sentiment_response = analyze_review_sentiments(
                review_detail['review'])
            if sentiment_response and 'sentiment' in sentiment_response:
                review_detail['sentiment'] = sentiment_response['sentiment']
            else:
                review_detail['sentiment'] = 'Unknown'
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message":
                             "Bad Request"}, status=400)

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):


def get_dealer_details(request, dealer_id):
    if (dealer_id):
        endpoint = "/fetchDealer/"+str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

# Create a `add_review` view to submit a review
# def add_review(request):


@csrf_exempt
def add_review(request):
    if not request.user.is_anonymous:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            logger.error(f"Error in posting review: {str(e)}")
            return JsonResponse({"status": 401, "message":
                                 "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})
