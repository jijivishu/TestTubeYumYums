# Python based imports
from datetime import date, datetime
from decimal import *

# Django based imports
from django_countries import countries
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm, TextInput, FloatField
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Internal imports
from .helpers import analyse
from .models import User, CBC, VitMin, CBCStat, VitMinStat, Range
from .serializers import RangeSerializer, CBCSerializer, VitMinSerializer, CBCStatSerializer, VitMinStatSerializer

# Imports
import json
import re

# Login existing user or register a new user
def authenticate_view(request):
    '''
    Takes in post request and decides whether to login or register the user based on 'formname' attribute of received json.
    '''
    if request.method == "POST":

        # Login form was submitted
        if json.loads(request.body)['formName'] == "Login":
            return login_view(request)
            
        # Register form was submitted
        elif json.loads(request.body)['formName'] == "Register":
            return register_view(request)
    
    return render(request, 'TestTubeYumYums/layout.html')


# Login view(only acts as a function) is called whenever an unauthenticated user requests login
def login_view(request):
    '''
    Validates login credentials. \n
    If credentials are valid, user is logged in and the landing page(views.index) is rendered. \n
    Otherwise, Json Response is returned containing error message.
    '''
    request_body = json.loads(request.body)
    email = request_body['email']
    password = request_body['password']

    # Check  if email is valid
    reg_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(reg_mail, email):

        # Check whether the database has a user with the received email
        if User.objects.filter(email=email).exists():

            # Validate the authenticity of password
            new_user = authenticate(email=email, password=password)
            if new_user is not None:

                # Login as the password successfully matches with entry in database
                login(request, new_user)
                return HttpResponseRedirect(reverse("index"))
            else:
                # Return message in response that request had incorrect password
                return JsonResponse({"message": "Incorrect Password"})
        else:
            # Return message in response that request had incorrect email
            return JsonResponse({"message": "Email is not registered with us"})
        
    else:
        # Return message in response that request had invalid email
        return JsonResponse({"message": "Invalid email"})


# Register view(only acts as a function) is called whenever an unauthenticated user requests registration
def register_view(request):
    '''
    Validates registration credentials. \n
    If credentials are valid, user is logged in and the landing page(views.index) is rendered.\n
    Otherwise, Json Response is returned containing error message.
    '''
    request_body = json.loads(request.body)

    # Every registration parameter from the body of request is loaded
    firstName = request_body['firstName']
    lastName = request_body['lastName']
    email = request_body['email']
    dob = request_body['dob']
    password = request_body['password']
    confirmation = request_body['confirmation']
    country = request_body['country']
    weight = request_body['weight']
    height = request_body['height']
    bp = request_body['bp']
    systolic = request_body['systolic']
    diastolic = request_body['diastolic']
    diabetes = request_body['diabetes']
    ast = request_body['ast']

    # An empty User instance is created to populate received data
    new_user = User()

    # Email field validation
    reg_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(reg_mail, email):

        # If the email is already present, response stating error message is sent
        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already in use"})
        else:
            new_user.email = email
    else:
        return JsonResponse({"message": "Invalid email"})
    
    # First Name field validation
    # Check if names aren't empty string
    if firstName == '':
        return JsonResponse({"message": "First Name is required"})
    else:
        # First Name is acceptable
        new_user.first_name = firstName

    # Last Name field validation
    if lastName == '':
        return JsonResponse({"message": "Last Name is required"})
    else:
        # Last Name is acceptable
        new_user.last_name = lastName

    # Date of Birth field validation
    # Check if dob is less than today's date
    # Since received dob is a string, convert it to datetime.date() object and thus validate it's format
    try:
        dob = datetime.date(datetime.strptime(dob, '%Y-%m-%d'))
        if date.today() >= dob:
            # Date is valid
            new_user.dob = dob
        else:
            return JsonResponse({"message": "Date of birth cannot be in future"})
    except ValueError:
        return JsonResponse({"message": "Date of birth must be in valid format"})

    # Password field validation
    # Check if password is valid
    reg_password = r'(?!^\d+$)^.{4,}'
    if re.fullmatch(reg_password, password):
        # Valid Password
        # Check if passwords are matching
        if password == confirmation:
            # Valid confirmation
            # Explicitly save password as hash
            new_user.set_password(password)
        else:
            return JsonResponse({"message": "Passwords must match"})
    else:
        return JsonResponse({"message": "Password must not be entirely numeric or less that 8 characters"})

    # Country field validation
    # Check if received country is valid
    if country != '':
        if country in dict(countries):
            # Country is valid
            new_user.country = country
        else:
            return JsonResponse({"message": "Country must be selected from dropdown list"})

    # Weight field validation
    # Check if received weight is valid
    if (weight != '' or weight != None or weight != '0') and weight :
        try:
            weight = round(Decimal(weight), 2)
            # Weight is valid
            new_user.weight = weight
        except Exception:
            return JsonResponse({"message": "Weight value must be a number (max two decimal places)"})

    # Height field validation
    # Check if received height is valid (None, 0, '')
    if (height != '' or height != None or height != '0') and height:
        try:
            height = round(Decimal(height), 2)
            # Height is valid
            new_user.height = height

            # If both height and weight are valid, calculate BMI (received values are in kg, cm)
            bmi = round(weight/(height*height)*10000, 2)
            new_user.bmi = bmi
        except Exception:
            return JsonResponse({"message": "Height value must be a number (max two decimal places)"})

    # Blood Pressure field validation
    # Check if user has blood pressure issues. If yes, check if both systolic and diastolic values are valid
    if bp == True:
        try:
            systolic = round(Decimal(systolic), 2)
            # Systolic is valid
            try:
                diastolic = round(Decimal(diastolic), 2)
                # Diastolic is valid
                new_user.bp = True
                new_user.systolic = systolic
                new_user.diastolic = diastolic
            except Exception:
                return JsonResponse({"message": "Diastolic value must be a number (max two decimal places)"})
        except Exception:
            return JsonResponse({"message": "Systolic value must be a number (max two decimal places)"})

    # Diabetes field validation
    # Check if user has diabetes. If yes, check whether AST values are valid
    if diabetes == True:
        try:
            ast = round(Decimal(ast), 2)
            # AST is valid
            new_user.diabetes = diabetes
        except Exception:
            return JsonResponse({"message": "AST value must be a number (max two decimal places)"})

    # New User instance is now populated with registration data, thus is saved.
    new_user.save()

    # A range object which is associated with customised test parameter range for each user, is created for new user 
    Range.objects.create(user=new_user)

    # New user is logged in and taken to the landing page
    login(request, new_user)
    return HttpResponseRedirect(reverse("index")) 


# Return country list to React file for rendering during new user registration
def countryList(request):
    '''
    Returns JSON response of all the countries with their country code as key
    '''
    return JsonResponse(dict(countries))


# Landing page view
def index(request): 
    '''
    Renders landing page populated with food suggestions for the logged user. \n
    Redirects for authentication in case of unauthenticated user.
    '''


    if request.user.is_authenticated:
        # Check if user has an object in CBCStat or VitMinStat
        cbc_found = CBCStat.objects.filter(user=request.user).exists()
        vitmin_found = VitMinStat.objects.filter(user=request.user).exists()
        cbc_upper = None
        cbc_lower = None
        vitmin_upper = None
        vitmin_lower = None

        # If no object is found, ask the user to enter test inputs in order to see personalized suggestions
        if not cbc_found and not vitmin_found:
            # Ask user to enter some values
            return render(request, 'TestTubeYumYums/layout.html', {
                "no_entries_yet": True
            })

        # If both CBCStat and VitMin Stat are found , query based on both
        elif cbc_found and vitmin_found:
            # Analyse both of them
            cbc_found = CBCStat.objects.filter(user=request.user).latest('id')
            vitmin_found = VitMinStat.objects.filter(user=request.user).latest('id')
            
        # If CBCStat found
        elif cbc_found:
            # Analyse only CBC
            cbc_found = CBCStat.objects.filter(user=request.user).latest('id')

        # If VitminStat found
        elif vitmin_found:
            # Analyse only vitmin
            vitmin_found = VitMinStat.objects.filter(user=request.user).latest('id')

        # Converting the queryset retreived into an ordered dictionary for ease of operation
        if cbc_found:
            data = CBCStatSerializer(cbc_found).data
            cbc_found = data['cbc']
            cbc_upper = data['upper_range']
            cbc_lower = data['lower_range']
        if vitmin_found:
            data = VitMinStatSerializer(vitmin_found).data
            vitmin_found = data['vitmin']
            vitmin_upper = data['upper_range']
            vitmin_lower = data['lower_range']

        report_analysis = analyse(cbc_found, cbc_lower, cbc_upper, vitmin_found, vitmin_lower, vitmin_upper)

        return render(request, 'TestTubeYumYums/layout.html', {
                "analysis": report_analysis["analysis"],
                "yum_yums": report_analysis['foods']
            })
    else:
        return HttpResponseRedirect(reverse("authenticate"))


@login_required
def logout_view(request):
    '''
    Logout the current authenticated user and redirect for authentication
    '''
    logout(request)
    return HttpResponseRedirect(reverse("authenticate"))


# Analysis
def analysis(request):
    '''
    No use for now, will be removed soon
    '''
    cbc_report = CBCStat.objects.filter(user=request.user).values_list('cbc', flat=True).order_by('-id')[:1]
    analyse(CBC.objects.filter(id=cbc_report).values())
    return HttpResponseRedirect(reverse("index"))


# Called whenever new set of test values are added by the user
@login_required
def add(request):
    '''
    Validates test values received through API \n

    If values are valid, data is updated in database and user is redirected to the landing page \n
    Otherwise, a respose is returned stating presence of invalid values. \n

    If the user is not online, a message is rendered asking them to be online for functional CDN React based front-end
    '''
    if request.method == 'POST':
        form_data = json.loads(request.body)['formData']

        # Check integrity of received data
        if not form_data['CBCStatus'] and not form_data['vitStatus'] and not form_data['minStatus']:
            return JsonResponse({"message": "Empty form cannot be submitted"})
        
        # Convert all the received values to Decimal, except null values which can remain empty
        for parameter in form_data:
            if isinstance(form_data[parameter], str):
                try:
                    form_data[parameter] = round(Decimal(form_data[parameter]), 3)
                except Exception:
                    return JsonResponse({"message": f"Invalid value submitted for {parameter}"})

        # Update respective database based on contents of received values
        # CBCStatus and vitStatus fields mark the presence of data for CBC model and VitMin model respectively
        if form_data['CBCStatus']:
            assign(request.user, CBC, CBCSerializer, form_data, "stat")

        if form_data['vitStatus'] or form_data['minStatus']:
            assign(request.user, VitMin, VitMinSerializer, form_data, "stat")

        # User is redirected to the home page after successful updation of database
        return HttpResponseRedirect(reverse("index"))
    else:
            return render(request, 'TestTubeYumYums/layout.html', {
                "form": "You need to be online for the website to be functional"
            })


# Sends the range of parameters to the frontend and updates them when asked to
@login_required
def paraRange(request):
    '''
    Range of parameters are fetched and updated within this view.
    '''
    if request.method == "POST":

        # Low parameters and high parameters are two clusters received irrespective of their category(CBC or VitMin)
        # All the received parameter values are converted into decimal
        low = json.loads(request.body)['low']
        for parameter in low:
            try:
                low[parameter] = round(Decimal(low[parameter]), 3)
            except Exception:
                return JsonResponse({"message": f"Value of {parameter} is invalid"})
            
        high = json.loads(request.body)['high']
        for parameter in high:
            try:
                high[parameter] = round(Decimal(high[parameter]), 3)
            except Exception:
                return JsonResponse({"message": f"Value of {parameter} is invalid"})
            
        # Fetch pre-existing values of range
        range = RangeSerializer(Range.objects.get(user=request.user))

        # Depending on which category of values are deviating, updated respective models
        if not check_match(range['cbc_lower'], low):
            # Lower range of CBC was altered
            assign(request.user, CBC, CBCSerializer, low, "low") 

        if not check_match(range['vitmin_lower'], low):
            # Lower range for vitmin was altered
            assign(request.user, VitMin, VitMinSerializer, low, "low")

        if not check_match(range['cbc_upper'], high):
            # Upper range for CBC was altered
            assign(request.user, CBC, CBCSerializer, high, "high")

        if not check_match(range['vitmin_upper'], high):
            # Upper range for vitmin was altered
            assign(request.user, VitMin, VitMinSerializer, high, "high")
        
        # When succesful, send response back to the client.
        return JsonResponse({"message": "Success"} )
    else:
        # Fetch range for each parameter and send it to the client
        range = Range.objects.get(user=request.user)
        serializer = RangeSerializer(range)
        return JsonResponse(serializer.data)


# Called to match pre-existing parameter range with received range
def check_match(default, received):
    '''
    Compares if default has same values as received for every parameter(except id)
    '''
    for parameter in default:
        # For value of each parameter in default, check if received has the same value for that parameter.
        name = parameter.name[(parameter.name.find('.') + 1):]
        value = round(Decimal(parameter.value), 2)

        # Skip id parameter since it won't match
        if name == "id":
            continue
        # Return wherever the first deviation is found
        if value.compare(received[name]):
            return False
    return True


# Called to update range of parameters for a user and also to create new test stat objects
def assign(user, model, serializer, received, type):
    '''
    For any given user, the functionality varies depending on the value of type argument. \n\n\n
    'low': Range object's model_lower parameter is updated depending on the value of model argument 
    (for updating lower range of parameters [by creating a new CBC or VitMin object]). \n\n
    'high': Range object's model_upper parameter is updated depending on the value of model argument 
    (for updating upper range of parameters [by creating a new CBC or VitMin object]). \n\n
    other: Depending on the value of model argument, new modelStat object is created 
    (for creating new object [CBC or VitMin] depending on test values entered by a user).\n\n

    Note: Range values or test values, both are basically an instance of CBC or VitMin model only. \n
    Refer models' schema for more info.
    '''

    # Create CBC or Vitmin object for new range or (set of test values)
    new_object = update_model(model, serializer, received)

    # Update Range model if called for range, else update Stat model as new test values are entered
    if model == CBC:
        if type == "low":
            Range.objects.filter(user=user).update(cbc_lower=new_object)
        elif type == "high":
            Range.objects.filter(user=user).update(cbc_upper=new_object)
        else:
            CBCStat.objects.create(user=user, cbc=new_object)
    if model == VitMin:
        if type == "low":
            Range.objects.filter(user=user).update(vitmin_lower=new_object)
        elif type == "high":
            Range.objects.filter(user=user).update(vitmin_upper=new_object)
        else:
            VitMinStat.objects.create(user=user, vitmin=new_object)


# Called to create entry in a model
def update_model(model, serializer, received):
    '''
    For any given model, this function creates a new object with every field(except id) based 
    on value of property, with same fieldname; retreived from received argument. \n\n

    Note: Only puropse of a serializer here is to get names of model fields. /n
    If you want certain fields to be untouched in created objects, provide a suitable ModelSerializer.
    '''

    # Create an empty instance of model
    new_object = model()
    # Obtain all fields througha serializer
    serialized = serializer(model())
    # For every field(except id), update the instance with respective value from received argument
    for field in serialized:
        name = field.name
        if name == "id":
            continue
        
        if name in received.keys():
            setattr(new_object, name, received[name])

    # Save the populated instance and then return it
    new_object.save()
    return new_object